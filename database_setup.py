from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Shelter(Base):
    _tablename_ = 'shelter'
    name = Column(String(80), nullable = False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipcode = Column(String(10))
    website = Column(String)
    id = Column(Integer, primary_key = True)


class Puppy(Base):
    _tablename_ = 'puppy'
    name = Column(String(250), nullable=False)
    gender = Column(String(6), nullable = False)
    dateOfBirth = Column(Date)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = Column(Numeric(10))
    id = Column(Integer, primary_key=True)


engine = create_engine(
'sqlite:///puppyshelter.db')


Base.metadata.create_all(engine)
