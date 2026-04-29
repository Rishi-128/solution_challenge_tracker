import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-auth.js";
import { getFirestore, doc, setDoc, getDoc, collection, onSnapshot, updateDoc } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-firestore.js";

// The standard Firebase hosting fetch for runtime config
let app;
let auth;
let db;

async function initFirebase() {
    try {
        const response = await fetch('/__/firebase/init.json');
        if (response.ok) {
            const config = await response.json();
            app = initializeApp(config);
        } else {
            console.warn("Could not fetch /__/firebase/init.json (Expected if not running via firebase serve). Falling back to placeholder.");
            app = initializeApp({
                projectId: "solution-challenge-tracker-dev",
                apiKey: "dummy-api-key"
            });
        }
    } catch (e) {
        console.error("Firebase init failed. Make sure you are running via 'firebase serve' or deployed to Firebase Hosting.", e);
    }

    auth = getAuth(app);
    db = getFirestore(app);
    return { app, auth, db };
}

// Ensure it is initialized before access
const firebaseInitPromise = initFirebase();

export { firebaseInitPromise, GoogleAuthProvider, signInWithPopup, onAuthStateChanged, signOut, doc, setDoc, getDoc, collection, onSnapshot, updateDoc };
