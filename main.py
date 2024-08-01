from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import models
from database import engine
from routes import post, user, auth, vote

# database.Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to SocialHub</title>
        <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .parallax {
                background-image: url('https://iili.io/dARyydv.jpg');
                height: 100vh; 
                background-attachment: fixed;
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
            .content {
                text-align: center;
                padding: 50px;
                background-color: rgba(255, 255, 255, 0.8);
            }
            h1 {
                color: #007acc;
            }
            p {
                color: #333;
            }
            a {
                color: #007acc;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="parallax"></div>
        <div class="content">
            <h1>Hello ALL, Welcome to FastAPI-SocialHub</h1>
            <p>Join us and connect with friends, share your moments, like posts, and much more!</p>
            <p>Discover new features and stay engaged in the community.</p>
            <div></div>
            <p></p>
            <p><a href="https://fastapi-a2sc.onrender.com/docs">Enter the App</a></p>
        </div>
    </body>
    </html>
    """
