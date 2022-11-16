import csv
import os
import shutil
import time
from tempfile import NamedTemporaryFile

import psycopg2
import psycopg2.extras
from fastapi import (BackgroundTasks, Depends, FastAPI, File, HTTPException,
                     UploadFile, status)
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


class registered(BaseModel):
    studentno: int
    lastname: str
    firstname: str
    middlename: str
    middleinitial: str
    nameextent: str
    college: str
    course: str
    yearlevel: int
    registrationcode: str
    permstreet: str
    permbarangay: str
    permsubmun: str
    permcity: str
    permprovince: str
    homestreet: str
    permzip: str
    homebarangay: str
    homesubmun: str
    homecity: str
    homeprovince: str
    homezip: str
    birthdate: str
    birthplace: str
    mobilenum: str
    gender: str
    plmemail: str
    emailadd: str
    motherlast: str
    motherfirst: str
    mothermiddle: str
    fatherlast: str
    fatherfirst: str
    fathermiddle: str

while True:

    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user='postgres', password = 'DBTIM140856',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print ("Database connection successfully")
        break
    except Exception as error:
        print ("Connection to database failed")
        print ("Error: ", error)
        time.sleep(2)


def find_datum(studentno):
    for datum in registered:
        if datum['studentno'] == studentno:
            return datum
def find_index_of_datum(studentno):
    for index, datum in enumerate(registered):
        if datum['studentno'] == studentno:
            return index


@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

'''
@app.get("/sqlalchemy")
def test_data(db: Session = Depends (get_db)):
    all_data = db.query(models.RegisteredData)
    print (all_data)
    return {"data": "successfully"}
'''

@app.get("/data")
def get_data():
    cursor.execute("""SELECT studentno,lastname,firstname,middlename,college,yearlevel,course FROM registered_data_full""")
    data_clean =cursor.fetchall()
    return {"data": data_clean}


#Register 1 Data
@app.post("/register", status_code=status.HTTP_201_CREATED)
def regis(name: registered,db: Session = Depends (get_db)):
    cursor.execute(""" INSERT into registered_data_full (studentno,lastname,firstname,middlename,middleinitial,nameextent,college,course,yearlevel,registrationcode,permstreet,permbarangay,permsubmun,permcity,permprovince,homestreet,permzip,homebarangay,homesubmun,homecity,homeprovince,homezip,birthdate,birthplace,mobilenum,gender,plmemail,emailadd,motherlast,motherfirst,mothermiddle,fatherlast,fatherfirst,fathermiddle) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)RETURNING * """, (name.studentno,name.lastname,name.firstname,name.middlename,name.middleinitial,name.nameextent,name.college,name.course,name.yearlevel,name.registrationcode,name.permstreet,name.permbarangay,name.permsubmun,name.permcity,name.permprovince,name.homestreet,name.permzip,name.homebarangay,name.homesubmun,name.homecity,name.homeprovince,name.homezip,name.birthdate,name.birthplace,name.mobilenum,name.gender,name.plmemail,name.emailadd,name.motherlast,name.motherfirst,name.mothermiddle,name.fatherlast,name.fatherfirst,name.fathermiddle))

    new_data = cursor.fetchone()
    conn.commit()
    return {"name": new_data}


# Get 1 Data
@app.get("/data/{studentno}")
def get_datum(studentno: str):
    cursor.execute("""SELECT * FROM registered_data_full WHERE studentno = %s""", (str(studentno),))
    find_data = cursor.fetchone()
    if not find_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"data with student number: {studentno} not found")
    return {"data": find_data}



@app.delete("/data/{studentno}",status_code=status.HTTP_204_NO_CONTENT)
def delete_datum(studentno: int):
    cursor.execute("""DELETE FROM registration_data WHERE studentno = %s returning *""", (str(studentno),))
    delete_data = cursor.fetchone()
    conn.commit()

    if delete_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"data with id: {studentno} not found")
    return {"message": "data deleted successfully"}


@app.put("/data/{studentno}")
def update_datum(studentno: str, name: registered):
    cursor.execute("""UPDATE registration_data SET lastname = %s,firstname = %s,middlename = %s,middleinitial = %s,nameextent = %s,college = %s,course = %s,yearlevel = %s,registrationcode = %s,permstreet = %s,permbarangay = %s,permsubmun = %s,permcity = %s,permprovince = %s,homestreet = %s,permzip = %s,homebarangay = %s,homesubmun = %s,homecity = %s,homeprovince = %s,homezip = %s,birthdate = %s,birthplace = %s,mobilenum = %s, gender = %s, plmemail = %s, emailadd = %s, motherlast = %s, motherfirst = %s, mothermiddle = %s,fatherlast = %s, fatherfirst = %s, fathermiddle = %s WHERE studentno = %s returning *""", (name.lastname,name.firstname,name.middlename,name.middleinitial,name.nameextent,name.college,name.course,name.yearlevel,name.registrationcode,name.permstreet,name.permbarangay,name.permsubmun,name.permcity,name.permprovince,name.homestreet,name.permzip,name.homebarangay,name.homesubmun,name.homecity,name.homeprovince,name.homezip,name.birthdate,name.birthplace,name.mobilenum,name.gender,name.plmemail,name.emailadd,name.motherlast,name.motherfirst,name.mothermiddle,name.fatherlast,name.fatherfirst,name.fathermiddle,str(studentno),))
    updated_data = cursor.fetchone()
    conn.commit()
    if updated_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"data with id: {studentno} not found")

    return {"data": updated_data}

'''
@app.get("/createtable")
def test_data(db: Session = Depends (get_db)):
    all_data = db.query(models.CleanData)
    print (all_data)
    return {"data": "successfully"}
'''

@app.put('/putdata')
async def load_data(db: Session = Depends (get_db)):
    all_data = db.query(models.RegisteredData)
    print (all_data)

    copy_table = """
        COPY registered_data_full FROM 'E:\\SE_Code\\data_freshie_all_final.csv' DELIMITER ',' CSV HEADER;
    """

    select_table = """
        SELECT * FROM registered_data_full;
    """

    cursor.execute(copy_table)
    cursor.execute(select_table)

    data = cursor.fetchall()
    json_data = []
    for row in data:
        json_data.append(dict(row))

    print(json_data)

    conn.commit()

    return {"message": "successfully"}






@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    with open(f'./{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}


