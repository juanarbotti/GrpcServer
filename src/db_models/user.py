from sqlalchemy import Column, Integer, String, Date
import ops.db as db

class User(db.Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, comment="Unique ID")
    name = Column(String(120), nullable=False, comment="User's Name")
    surname = Column(String(120), nullable=False, comment="User's Surname")
    dob = Column(Date(), nullable=True, default=None, comment="User's Date of Birth") # optional value
    gender = Column(String(32), nullable=True, default=None, comment="User's Gender") # optinal value
    username = Column(String(20), nullable=False, comment="User's Username")
    email = Column(String(320), nullable=False, comment="User's Email")
    password = Column(String(60), nullable=False, comment="User's Password (hashed)") # bcrpt creates a 60 character long hashed password