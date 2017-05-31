import sys
from sqlalchemy import
Column, ForeignKey, Integer, SUBSTRING
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine(
'sqlite:///puppies.db')

Base.metadata.create_all(engine)
