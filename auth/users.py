from sqlalchemy import Column, Integer, String
from db.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index=True)
    username = Column(String, unique = True)
    password_hash = Column(String)
    role = Column(String, default="analyst") # We can later on define other roles like admin, analyst