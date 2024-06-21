import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
from fuzzywuzzy import process
from firebase_config import db 

def find_matching_jobs(query: str, limit: int = 5):
    """Find jobs matching the query using fuzzy matching from the job_posts collection."""
    collection_name = 'job_posts'
    docs = db.collection(collection_name).stream()

    job_names = []
    job_data = []

    for doc in docs:
        data = doc.to_dict()
        job_names.append(data.get('job_name'))
        job_data.append(data)

    matches = process.extract(query, job_names, limit=limit)
    matched_jobs = [job_data[job_names.index(match[0])] for match in matches if match[1] >= 50]

    return matched_jobs


def get_all_job_openings():
    '''This is used to return all job openings'''
    collection_name = 'job_posts'
    docs = db.collection(collection_name).stream()

    job_openings = [doc.to_dict() for doc in docs]

    return job_openings



