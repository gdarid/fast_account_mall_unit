""" Sqlalchemy models : for database """
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    malls = relationship("Mall", back_populates="owner")


class Mall(Base):
    __tablename__ = "mall"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("account.id"))

    owner = relationship("Account", back_populates="malls")

    units = relationship("Unit", back_populates="mall")


class Unit(Base):
    __tablename__ = "unit"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mall_id = Column(Integer, ForeignKey("mall.id"))

    mall = relationship("Mall", back_populates="units")
