from fastapi import status, HTTPException, Depends, APIRouter
import models, schemas, utils
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix= "/users", # + /id
    tags= ['Users']
)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user : schemas.UserCreate, db : Session = Depends(get_db)):
    #hashing the password = user.password
    user.password = utils.hash(user.password)
    new_user = models.User(**(dict(user)))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=schemas.UserOut)
def getUser(id : int, db : Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with Id - {id} not found")

    return user