
from database import Base
# import database
from sqlalchemy import Column, Integer, Boolean,String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

# Creating Tables using Python without Actual Postgres
# this is alchmry model -> which specifies only how table looks like
class Post(Base):
    __tablename__ = "posts"

    #if table name exists the this class will not modify 
    # anything in this table names "posts"
    # to update we use "ALEMBIC" module

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, nullable = False, server_default = "TRUE")
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, 
                        server_default=text('now()'))
    # Adding Foriegn Key Constraint using SQLAlchemy
    owner_id = Column(Integer, 
                      ForeignKey("users.id", 
                      ondelete="CASCADE"), 
                      nullable=False)
    
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, nullable = False)
    email = Column(String, nullable=False, unique=True)
    password= Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text('now()'))

class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)