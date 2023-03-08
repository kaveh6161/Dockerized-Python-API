from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/{user_id}")
def read_user(user_id: int, q: str = None):
    # Define sample user data
    users = {
        1: {"name": "Kaveh", "email": "kaveh@god.dev"},
        2: {"name": "Donatas", "email": "donatas@god.dev"},
        3: {"name": "Ramunas", "email": "ramunas@god.dev"},
        4: {"name": "Romas", "email": "romas@god.dev"}
    }

    # Fetch user data for the provided user_id
    user_data = users.get(user_id)

    # Add any additional processing logic here
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Return the user data as a JSON response
    return user_data

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str):
    # Define sample user data
    users = {
        1: {"name": "Kaveh", "email": "kaveh@god.dev"},
        2: {"name": "Donatas", "email": "donatas@god.dev"},
        3: {"name": "Ramunas", "email": "ramunas@god.dev"},
        4: {"name": "Romas", "email": "romas@god.dev"}
    }

    # Update the user data for the provided user_id
    user_data = users.get(user_id)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_data["name"] = name
    user_data["email"] = email

    # Return the updated user data as a JSON response
    return user_data

@app.patch("/users/{user_id}")
def patch_user(user_id: int, name: str = None, email: str = None):
    # Define sample user data
    users = {
        1: {"name": "Kaveh", "email": "kaveh@god.dev"},
        2: {"name": "Donatas", "email": "donatas@god.dev"},
        3: {"name": "Ramunas", "email": "ramunas@god.dev"},
        4: {"name": "Romas", "email": "romas@god.dev"}
    }

    # Update the user data for the provided user_id
    user_data = users.get(user_id)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    if name:
        user_data["name"] = name
    if email:
        user_data["email"] = email

    # Return the updated user data as a JSON response
    return user_data

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    # Define sample user data
    users = {
        1: {"name": "Kaveh", "email": "kaveh@god.dev"},
        2: {"name": "Donatas", "email": "donatas@god.dev"},
        3: {"name": "Ramunas", "email": "ramunas@god.dev"},
        4: {"name": "Romas", "email": "romas@god.dev"}
    }
    # Delete the user data for the provided user_id
    user_data = users.pop(user_id, None)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Return a message indicating that the user was deleted
    return {"message": "User deleted"}
