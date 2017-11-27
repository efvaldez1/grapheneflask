from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()

class Category(Base):
	__tablename__="department"
	id = Column(Integer,primary_key=True)
	name = Column(String)

class Product(Base):
	__tablename__="employee"
	id=Column(Integer,primary_key=True)
	description=Column(String)
	author = Column(String)
	name = Column(String)
	added_on = Column(DateTime,default=func.now())
	category_id = Column(Integer,ForeignKey('category.id'))
	category=relationship(Category,backref=backref("employees",uselist=True,cascade='delete,all'))

class Offer(Base):
	__tablename__="offer"
	id=Column(Integer,primary_key)
	amount = Column(Float)
	offerDescription = Column(String)
	product_id = Column(Integer,ForeignKey('product.id'))
	product=relationship(Product,backref=backref("products",uselist=True,cascade='delete,all'))	
