#!/usr/bin/python3
""" a script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    list = session.query(State.name, City.id, City.name).\
           fiter(State.id == City.state_id)
    for location in list:
        print("{}: ({}) {}".format(location[0], location[1], location[2]))
