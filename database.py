from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserverorhost/db_name"
# SQLALCHEMY_DATABASE_URL = f"postgresql://{
#     settings.DATABASE_USERNAME}:{
#         settings.DATABASE_PASSWORD}@{
#             settings.DATABASE_HOSTNAME}:{
#                 settings.DATABASE_PORT}/{
#                     settings.DATABASE_NAME}"
SQLALCHEMY_DATABASE_URL = (
    "postgresql://"
    + settings.DATABASE_USERNAME + ":"
    + settings.DATABASE_PASSWORD + "@"
    + settings.DATABASE_HOSTNAME + ":"
    + str(settings.DATABASE_PORT) + "/"
    + settings.DATABASE_NAME
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, 
                            autoflush=False, 
                            bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()

# while True:
#     try :
#         conn = psycopg2.connect(host="localhost" ,dbname="fastapi", user="postgres", password="root",
#                                 cursor_factory=RealDictCursor )
#         cursor = conn.cursor()
#         print("Database Connected Successfully")
#         break
#     except Exception as error:
#         print("Database Connection was Unsuccessfull")
#         print(f"Error : {error}")
#         time.sleep(2)
