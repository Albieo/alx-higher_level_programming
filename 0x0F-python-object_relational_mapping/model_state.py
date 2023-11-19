#!/usr/bin/python3
""" a python file that contains the class definition
of a State and an instance Base = declarative_base() """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """ Class definition of State model """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
