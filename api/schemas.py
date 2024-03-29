"""Schemas (pydantic models) : for requests/responses"""
from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class UnitInit(BaseModel):
    name: str


class UnitCreate(UnitInit):
    mall_id: Optional[int]


class Unit(UnitInit):
    id: int
    mall_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)


class MallInit(BaseModel):
    name: str


class MallCreate(MallInit):
    owner_id: Optional[int]


class Mall(MallInit):
    id: int
    owner_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)


class AccountInit(BaseModel):
    name: str


class AccountCreate(AccountInit):
    pass


class Account(AccountInit):
    id: int
    malls: List[Mall] = []

    model_config = ConfigDict(from_attributes=True)
