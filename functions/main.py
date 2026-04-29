import os
import json
import csv
import io
import datetime
from firebase_functions import firestore_fn, https_fn
from firebase_admin import initialize_app, firestore, auth
from google.cloud import bigquery

initialize_app()

db = firestore.client()

def send_email(to_emails, subject, content, new_stage=None):
    for email in to_emails:
        if new_stage:
            print(f"[EMAIL LOG] Sending email to {email} - Stage updated to {new_stage}")
        else:
            print(f"[EMAIL LOG] Sending email to {email} - {subject}")

@firestore_fn.on_document_updated(document="teams/{teamId}")
def on_stage_update(event: firestore_fn.Event[firestore_fn.Change[firestore_fn.DocumentSnapshot]]) -> None:
    old_data = event.data.before.to_dict() or {}
    new_data = event.data.after.to_dict() or {}
    
    old_stage = old_data.get("stage")
    new_stage = new_data.get("stage")
    
    if old_stage != new_stage:
        print(f"Stage changed for {event.params['teamId']} from {old_stage} to {new_stage}")
        
        # 1. Send Email
        members = new_data.get("members", [])
        to_emails = [m.get("email") for m in members if m.get("email")]
        if to_emails:
            subject = f"Your Team Stage Updated to '{new_stage}'"
            content = f"<p>Great job! Your team <strong>{new_data.get('teamName', 'Team')}</strong> is now at the <strong>{new_stage}</strong> stage.</p>"
            send_email(to_emails, subject, content, new_stage)
            
        # 2. Log to BigQuery
        project_id = os.environ.get('GCLOUD_PROJECT', 'solution-challenge-tracker-dev')
        bq_client = bigquery.Client(project=project_id)
        table_id = f"{project_id}.tracker_analytics.stage_events"
        
        rows_to_insert = [
            {
                "team_id": event.params['teamId'],
                "team_name": new_data.get("teamName", ""),
                "old_stage": old_stage,
                "new_stage": new_stage,
                "timestamp": datetime.datetime.utcnow().isoformat()
            }
        ]
        try:
            bq_client.insert_rows_json(table_id, rows_to_insert)
        except Exception as e:
            print(f"Error inserting to BigQuery (Make sure table exists): {e}")


@https_fn.on_request()
def deadline_reminder(req: https_fn.Request) -> https_fn.Response:
    # Query all teams where stage is not Submitted or Finalist
    docs = db.collection("teams").where(filter=firestore.FieldFilter("stage", "not-in", ["Submitted", "Finalist"])).stream()
    
    emails_sent_count = 0
    for doc in docs:
        team_data = doc.to_dict()
        members = team_data.get("members", [])
        to_emails = [m.get("email") for m in members if m.get("email")]
        if to_emails:
            subject = "Action Required: Solution Challenge Submission Deadline"
            content = f"<p>Hello Team <strong>{team_data.get('teamName', 'Team')}</strong>,</p><p>This is a reminder that the deadline is approaching. Please ensure your project is submitted.</p>"
            send_email(to_emails, subject, content)
            emails_sent_count += 1
            
    return https_fn.Response(json.dumps({"status": "success", "emails_sent": emails_sent_count}), status=200, mimetype="application/json")


@https_fn.on_request()
def export_teams_csv(req: https_fn.Request) -> https_fn.Response:
    auth_header = req.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
         return https_fn.Response("Unauthorized", status=401)
         
    token = auth_header.split("Bearer ")[1]
    
    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token["uid"]
    except Exception as e:
        return https_fn.Response(f"Unauthorized: {e}", status=401)
        
    # Check if user is organizer
    user_doc = db.collection("users").document(uid).get()
    if not user_doc.exists or user_doc.to_dict().get("role") != "organizer":
        return https_fn.Response("Forbidden: Admins only", status=403)
        
    # Generate CSV
    docs = db.collection("teams").stream()
    
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['Team Name', 'College', 'Track', 'Project Title', 'Stage', 'Members Count', 'Created At'])
    
    for doc_snap in docs:
        data = doc_snap.to_dict()
        cw.writerow([
            data.get('teamName', ''),
            data.get('college', ''),
            data.get('track', ''),
            data.get('projectTitle', ''),
            data.get('stage', ''),
            len(data.get('members', [])),
            data.get('createdAt', '')
        ])
        
    response = https_fn.Response(si.getvalue(), status=200, mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=teams_export.csv"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
