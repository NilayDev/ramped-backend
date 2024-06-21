import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS')
# Use the service account key file
cred = credentials.Certificate(FIREBASE_CREDENTIALS) 
firebase_admin.initialize_app(cred)

db = firestore.client()

# Read CSV file
csv_file_path = '/pathto/Example job post data.csv'
data = pd.read_csv(csv_file_path)

# Clean the data: remove columns with all NaN values and replace 'Null' with None
data = data.replace({'Null': None})

# Convert DataFrame to dictionary format
data_dict = data.to_dict(orient='records')

# Create a new collection and add documents
collection_name = 'job_posts'
for record in data_dict:
    doc_ref = db.collection(collection_name).document(record['post_id'])
    doc_ref.set(record)

print(f'Imported {len(data_dict)} records into Firestore collection "{collection_name}".')
