from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# this tell passlib to use
#bcrypt --> as Hashing Algorithm

def hash(password : str):
    hash_password = pwd_context.hash(password)
    password = hash_password
    return password

def verify(palin_password , hashed_password):
    return pwd_context.verify(palin_password, hashed_password)