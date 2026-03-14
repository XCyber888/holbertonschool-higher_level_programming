#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base obyektini yaradırıq, bütün klasslar bundan miras alacaq
Base = declarative_base()


class State(Base):
    """
    State class inherits from Base and links to the MySQL table states
    """
    __tablename__ = 'states'
    
    # id sütunu: auto-generated, unique integer, not null, primary key
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    
    # name sütunu: string max 128 characters, not null
    name = Column(String(128), nullable=False)
