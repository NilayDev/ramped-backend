from fastapi import HTTPException
from passlib.context import CryptContext
from models import User
from firebase_config import db  # Import the db object from firebase_config
from jwt_handler import create_access_token

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    '''Hashed the Password'''
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    '''To verify the password'''
    return pwd_context.verify(plain_password, hashed_password)

def create_user(user: User):
    """Create a new user in the database."""
    user_ref = db.collection('users').document(user.email)
    if user_ref.get().exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    user_ref.set({
        'email': user.email,
        'password': hashed_password,
        'token': None
    })
    return {"message": "User created successfully"}

def authenticate_user(email: str, password: str):
    """Authenticate a new user."""
    user_ref = db.collection('users').document(email)
    user_doc = user_ref.get()
    if not user_doc.exists:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    user_data = user_doc.to_dict()
    if not verify_password(password, user_data['password']):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Generate JWT token
    access_token = create_access_token(data={"sub": email})
    
    # Store token in Firestore
    user_ref.update({"token": access_token})
    
    return {"message": "Login successful", "access_token": access_token}


