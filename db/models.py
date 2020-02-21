from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from .db import Base

association_table = Table('association', Base.metadata,
    Column('person_id', Integer, ForeignKey('people.id')),
    Column('project_id', Integer, ForeignKey('projects.id'))
)

class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    projects = relationship("Project", secondary=association_table, back_populates="people")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    people = relationship("Person", secondary=association_table, back_populates="projects")


