import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

load_dotenv()

FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS')
# Use the service account key file
cred = credentials.Certificate(FIREBASE_CREDENTIALS) 
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
print(db)
