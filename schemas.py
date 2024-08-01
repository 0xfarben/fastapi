from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic import conint
from datetime import datetime
# THis is the Pydantic Model
# Also referred to as Schema
# class Post(BaseModel):
#     title : str
#     content : str
#     published : bool = True

# class CreatePost(BaseModel):
#     title : str
#     content : str
#     published : bool = True

# class UpdatePost(BaseModel):
#     title : str
#     content : str
#     published : bool

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True

#Inheritance
class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    class Config:
        orm_mode = True
        
class Post(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : UserOut
    # Pydantic's "orm_mode" will tell the Pydantic model to read the data 
    # even if it is not a dict, but an ORM model 
    # (or any other arbitrary object with attributes).
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post : Post
    votes : int

    class COnfig:
        orm_mode = True

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserLogin(BaseModel):
    email :EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None

class Vote(BaseModel):
    post_id : int
    dir : conint(le=1) # type: ignore
