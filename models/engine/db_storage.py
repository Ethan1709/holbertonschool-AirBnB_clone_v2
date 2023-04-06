#!/usr/bin/python3
""" Define class DBStorage """
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, close_all_sessions
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{} {}"
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""

        from models.base_model import Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.state import State

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        close_all_sessions(self)
