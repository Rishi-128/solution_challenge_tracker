# Solution Challenge Tracker

A fully functional web application designed for the Google Developer Student Clubs (GDSC) Solution Challenge. This tracker empowers student participants to register their teams, update their project milestones, and monitor global impact, while providing organizers with a dedicated dashboard to track submissions and export data.

## Features

- **Participant Dashboard**: Track journey progress, update current submission stages, and manage team rosters.
- **Organizer Dashboard**: View real-time analytics on total teams, submitted projects, and top tracks. Includes a sortable team directory and CSV export functionality.
- **Global Impact**: Live tracking of global participation metrics and prototypes built to solve the UN Sustainable Development Goals.
- **Teams Directory**: A public hub to discover all participating teams, their colleges, and current progress.
- **Premium UI/UX**: Built with a sleek, modern glassmorphism design system, smooth CSS keyframe animations, and highly interactive components.
- **Authentication**: Seamless Google Sign-In via Firebase Auth.
- **Real-Time Data**: Powered by Firebase Firestore for instant updates across all clients.

## Tech Stack

- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS (via CDN)
- **Backend & Database**: Firebase (Authentication, Firestore Database, Hosting)
- **Cloud Functions**: Python (for secure CSV exports and backend tasks)
- **Design System**: Custom Glassmorphism UI with Tailwind utility classes

## Project Structure

```text
solution_challenge_tracker/
├── firebase.json              # Firebase project configuration and hosting rules
├── firestore.rules            # Security rules for Firestore database
├── firestore.indexes.json     # Database index configurations
├── frontend/                  # Web Application Source Code
│   ├── js/
│   │   └── firebase-config.js # Shared Firebase SDK initialization
│   ├── landing_page/          # Entry point and login screen
│   ├── register_team/         # Team registration and onboarding flow
│   ├── participant_dashboard/ # Main dashboard for team members
│   ├── organizer_dashboard/   # Admin dashboard for event organizers
│   ├── teams/                 # Public directory of registered teams
│   ├── impact/                # Global analytics and SDG tracking
│   └── resources/             # Developer documentation links
└── functions/                 # Firebase Cloud Functions (Python)
    ├── main.py
    └── requirements.txt
```

## Getting Started

### Prerequisites

1. A [Firebase account](https://firebase.google.com/)
2. [Firebase CLI](https://firebase.google.com/docs/cli) installed globally (`npm install -g firebase-tools`)
3. Python 3.10+ (for deploying Cloud Functions)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rishi-128/solution_challenge_tracker.git
   cd solution_challenge_tracker
   ```

2. **Connect to your Firebase Project:**
   ```bash
   firebase login
   firebase use --add
   ```
   *Select your created Firebase project.*

3. **Update Firebase Configuration:**
   If you created a new Firebase project, update the `firebaseConfig` object located in `frontend/js/firebase-config.js` with your project's credentials from the Firebase Console.

4. **Run Locally:**
   Use the Firebase emulators or serve the hosting directory locally to test:
   ```bash
   firebase serve --only hosting
   ```

### Deployment

To deploy the frontend to Firebase Hosting:

```bash
firebase deploy --only hosting
```

To deploy the backend Cloud Functions:

```bash
firebase deploy --only functions
```

## Security Rules

Ensure your Firestore database rules are configured correctly to secure participant data. The `firestore.rules` file contains the baseline role-based access control for this platform, ensuring only organizers have read-all permissions, while participants can only read/write to their specific team documents.
