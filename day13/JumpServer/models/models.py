from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Host(Base):
    pass