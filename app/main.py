from fastapi import FastAPI
import app.models as models
# import database
from app.database import engine
from app.routes import post, user, auth, vote

# database.Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")  
async def root():
    return {"message": "Hello ALL, Welcome to the World Of APIs"}