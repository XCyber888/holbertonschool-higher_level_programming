#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Engine yaradırıq
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    # Session klassını yaradırıq və engine-ə bağlayırıq
    Session = sessionmaker(bind=engine)
    session = Session()

    # Bütün State-ləri id-yə görə sıralayıb çəkirik
    states = session.query(State).order_by(State.id).all()

    # Nəticələri çap edirik
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Session-ı bağlayırıq
    session.close()
