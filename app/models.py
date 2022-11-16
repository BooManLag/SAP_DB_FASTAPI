from .database import Base
from sqlalchemy.sql.expression import null
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class RegisteredData(Base):
    __tablename__ = "registered_data_full"

    studentno = Column(Integer, primary_key=True,nullable=False)
    lastname = Column(String,nullable=False)
    firstname = Column(String,nullable=False)
    middlename = Column(String,nullable=True)
    middleinitial = Column(String,nullable=True)
    nameextent = Column(String,nullable=True)
    college = Column(String,nullable=False)
    course = Column(String,nullable=False)
    yearlevel = Column(Integer,nullable=False)
    registrationcode = Column(String,nullable=False)
    permstreet = Column(String,nullable=True)
    permbarangay = Column(String,nullable=True)
    permsubmun = Column(String,nullable=True)
    permcity = Column(String,nullable=True)
    permprovince = Column(String,nullable=True)
    homestreet = Column(String,nullable=True)
    permzip = Column(String,nullable=True)
    homebarangay = Column(String,nullable=True)
    homesubmun = Column(String,nullable=True)
    homecity = Column(String,nullable=True)
    homeprovince = Column(String,nullable=True)
    homezip = Column(String,nullable=True)
    birthdate = Column(String,nullable=True)
    birthplace = Column(String,nullable=True)
    mobilenum = Column(String,nullable=True)
    gender = Column(String,nullable=True)
    plmemail = Column(String,nullable=True)
    emailadd = Column(String,nullable=True)
    motherlast = Column(String,nullable=True)
    motherfirst = Column(String,nullable=True)
    mothermiddle = Column(String,nullable=True)
    fatherlast = Column(String,nullable=True)
    fatherfirst = Column(String,nullable=True)
    fathermiddle = Column(String,nullable=True)


class CleanData(Base):
    __tablename__ = "try_full_data"

    studentno = Column(Integer, primary_key=True,nullable=False)
    lastname = Column(String,nullable=False)
    firstname = Column(String,nullable=False)
    middlename = Column(String,nullable=False)
    middleinitial = Column(String,nullable=False)
    nameextent = Column(String)
    college = Column(String,nullable=False)
    course = Column(String,nullable=False)
    yearlevel = Column(Integer,nullable=False)