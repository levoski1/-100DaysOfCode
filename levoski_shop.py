#!/usr/bin/python3

''' sqlalchemy is a library in python.
    ORM is a Module in sqlalchemy
    create_engine is a function used to create a connection to a database
    Session is class that represents a transactional context for communicating with a database
    declarative_base  returns a base class for declarative class definitions. 
'''
from sqlalchemy import create_engine, Column, String, Integer,DateTime, Enum, ForeignKey
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

# let's Define your table class schema
class Users(Base):
        __tablename__ = 'customer'

        id = Column(Integer, primary_key=True,autoincrement=True)
        first_name = Column(String(20),nullable=False)
        last_name = Column(String(20),nullable=False)
        email = Column(String(55), unique=True, nullable=False)
        gender = Column(Enum('male','female',name = 'gender_name'))
        city = Column(String(15), nullable=False)
        created_at = Column(DateTime(), default=datetime.now())
        order = relationship('Order',back_populates = 'customer')
       
        
class Order(Base):
        __tablename__ = 'order'

        order_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
        customer_id = Column(Integer, ForeignKey('customer.id'))
        order_date = Column(DateTime(), default=datetime.now(),nullable=False)
        status = Column(Enum('pending', 'processing', 'delivered',name = 'order_status'))
        payment_method = Column(Enum('credit card','paypal', name = 'pay_method'))
        customer = relationship('Customer' , back_populates = 'order')
        
# Connect to the database
engine = create_engine("mysql+mysqldb://root:9857@localhost/e_commerce")


# creates the tables if not exists in the database
Base.metadata.create_all(engine)


# lets create session and bind our engine
session = Session(bind=engine)
        


# creating the customer's table records
cust_1 = Users(
        first_name = 'Ugwoke',
        last_name = 'levi',
        email = 'levisoromto1@gmail.com',
        gender = 'male',
        city = 'Enugu',
        
)

cust_2 = Users(
        first_name = 'Abugu',
        last_name = 'chidera',
        email = 'abuguchidera@gmail.com',
        gender = 'male',
        city = 'Cross River',
        
)

cust_3 = Users(
        first_name = 'Gbemi',
        last_name = 'Gbeminiyi',
        email = 'gbeminiyi@gmail.com',
        gender = 'male',
        city = 'lagos',
        
)

cust_4 = Users(
        first_name = 'Uduka',
        last_name = 'kings',
        email = 'udukakings@gmail.com',
        gender = 'male',
        city = 'porthacort',
        
)

cust_5 = Users(
        first_name = 'Asogwa',
        last_name = 'leno',
        email = 'asogwaleno@gmail.com',
        gender = 'female',
        city = 'Benin',
        
)


# creating customer order table
order_1 = Order(
       # total_amount = '4500',
        status = 'pending',
        payment_method = 'cash',
        
)


session.add_all([cust_1,cust_2,cust_3,cust_4,cust_5,order_1])
session.commit()

session.close()













'''
                BASIC KNOWLEDGE
1. Session is a class provided by SQLAlchemy that represents a connection to the database. Instances of Session are used to perform CRUD (Create, Read, Update, Delete) operations on your database tables

2. Declative_base is a function. It's a template that helps us define how each table should look.
So, when we want to create a new table, we use this template (the declarative base) to make our job easier. 

3. relationship(): This is a function provided by SQLAlchemy to define relationships between classes.
'''