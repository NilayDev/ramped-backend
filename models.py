from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class JobQuery(BaseModel):
    query: str =""
    limit: int = 5