from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdateRequest
from uuid import UUID, uuid4
from typing import Optional, List

app = FastAPI() # Creating an instance of the Application. So to start it, we use "uvicorn main:app --reload"

# This is database which is a list of users. It currently has two users
db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Olaoluwa",
        last_name="Olayokun",
        email="olaoluwa.olayokun@cloudcolonyng.com", 
        gender=Gender.male, 
        roles=[Role.student]
    ),
    User(
        id=uuid4(), 
        first_name="Morenikeji",
        last_name="Olayokun",
        email="keji.olayokun@cloudcolonyng.com", 
        gender=Gender.female, 
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")   # This gives a route for a GET request which path is the root in this case
async def root():
    return {"Hello": "Edmundo"}

@app.get("/api/v1/users")   # This path fetches list of all users.
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):    # This accepts a payload of user with type User
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        detail=f"User with the id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:     # Check whether user is in Database
        if user.id == user_id:
            if user_update.first_name is not None:      # Checks if the value is not None
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.email is not None:
                user.email = user_update.email
            if user_update.gender is not None:
                user.gender = user_update.gender
            return
    raise HTTPException(
        status_code=404,    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        detail=f"User with the id: {user_id} does not exist"
    )