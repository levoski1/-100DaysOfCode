#!/usr/bin/python3OA

''' sqlalchemy is a library in python.
    ORM is a Module in sqlalchemy
    create_engine is a function used to create a connection to a database
    Session is class that represents a transactional context for communicating with a database
    declarative_base  returns a base class for declarative class definitions. 
'''
from sqlalchemy import create_engine, Column, String, Integer,DateTime, Enum
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine("mysql+mysqldb://root:9857@localhost/e_commerce",echo=True)

# lets create session and bind our engine
session = Session(bind=engine)


Base = declarative_base()

# let's Define your table class
class Users(Base):
        __tablename__ = 'customers'

        id = Column(Integer, primary_key=True,autoincrement=True)
        first_name = Column(String(20),nullable=False)
        last_name = Column(String(20),nullable=False)
        email = Column(String(25), unique=True, nullable=False)
        Phone_Number = Column(String(15)cd,nullable=True)
        gender = Column(Enum('male','female',name = 'gender_name'))
        city = Column(String(15), nullable=False)
        created_at = Column(DateTime(), default=datetime.now())


# creates the tables if not exists
Base.metadata.create_all(engine)

# creating the records
record1 = Users(
        first_name = 'Ugwoke',
        last_name = 'levi',
        email = 'levisoromto1@gmail.com',
        Phone_Number = '09033887693',
        gender = 'male',
        city = 'Enugu',
        
)


session.add(record1)
session.commit()


















'''
                BASIC KNOWLEDGE
1. Session is a class provided by SQLAlchemy that represents a connection to the database. Instances of Session are used to perform CRUD (Create, Read, Update, Delete) operations on your database tables

2. Declative_base is a function. It's a template that helps us define how each table should look.
So, when we want to create a new table, we use this template (the declarative base) to make our job easier. 
'''