from fastapi import FastAPI
import models
# import database
from database import engine
from routes import post, user, auth, vote

# database.Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")  
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
        <style>
            body {
                background-color: #f0f8ff; /* Light blue background color */
                color: #333; /* Dark text color */
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #007acc; /* Blue text color for heading */
            }
        </style>
    </head>
    <body>
        <h1>Hello ALL, Welcome to the World Of APIs</h1>
        <p>Explore the fascinating world of APIs and their applications!</p>
    </body>
    </html>
    """
