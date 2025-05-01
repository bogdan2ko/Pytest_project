from sqlalchemy.orm import sessionmaker
from configuration import CONNECTION_RAW
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base(name='Model')

engine = create_engine(CONNECTION_RAW)

Session = sessionmaker(engine, autoflush=False, autocommit=False)

session = Session()