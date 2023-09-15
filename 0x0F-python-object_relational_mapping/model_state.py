#!/usr/bin/python3
""" This module represents the State class """

from uuid import uuid4
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, MetaData

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """ Class for the State schema"""
    __tablename__ = "states"

    id = Column(Integer,
                primary_key=True,
                nullable=True,
                unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=True)
