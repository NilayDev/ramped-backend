from fastapi import FastAPI, Depends
from pydantic import BaseModel
from auth import create_user, authenticate_user
from fuzzy_match import find_matching_jobs, get_all_job_openings
from models import User, JobQuery
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserIn(BaseModel):
    email: str
    password: str

@app.post("/signup")
def signup(user: UserIn):
    '''API for sign up '''
    return create_user(User(email=user.email, password=user.password))

@app.post("/login")
def login(user: UserIn):
    '''API for Login '''
    return authenticate_user(user.email, user.password)


@app.post("/job_match")
async def job_match(query: JobQuery):
    '''API for Job Match '''
    print(query.query)
    if query.query:
        return find_matching_jobs(query.query)
    else:
        return get_all_job_openings()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
