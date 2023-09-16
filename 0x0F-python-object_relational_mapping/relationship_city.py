#!/usr/bin/python3
""" This module represents the City class """

from sqlalchemy import Column, String, Integer, ForeignKey

from relationship_state import Base


class City(Base):
    """ Class for the State schema"""
    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True,
                nullable=True,
                unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    # state = relationship("State", back_populates="cities")
