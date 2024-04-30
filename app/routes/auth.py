from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import database
import schemas
import models
import utils
import oauth

router=  APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model=schemas.Token)
def login(user_cred: OAuth2PasswordRequestForm= Depends(),
          db : Session = Depends(database.get_db)):

    # OAuth2PasswordRequestForm is differnet type of dict
    # it takes input thourgh FORM-DATA see POSTMAN
    {
        "username" : "asfa",
        "password" : "sadsad"
    }
    #OLD
    # user = db.query(models.User).filter(models.User.email == user_cred.email).first()

    #NEW
    user = db.query(models.User).filter(models.User.email == user_cred.username).first()

    # Password Checking
    #if password not correct
    if not user :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Invalid Credentials')

    if not utils.verify(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Invalid Credentials')

    # If password is correct
    # Create JWT TOken
    access_token = oauth.create_access_token(data = {
        "user_id" : user.id
    })

    return {"access_token" : access_token,
            "token_type" : "bearer"}