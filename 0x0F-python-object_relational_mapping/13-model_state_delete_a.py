#!/usr/bin/python3
""" 13-model_state_delete_a
Module that connects with the hbtn_0e_6_usa database and deletes all State
objects with a name containing the letter 'a' from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.ilike('%a%')).all():
        session.delete(state)
    # session.delete(session.query(State).filter_by(id=8).first())
    session.commit()
    session.close()