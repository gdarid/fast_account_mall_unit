from sqlalchemy.orm import Session
from . import models, schemas


# Accounts
def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()


def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    nb_rows = db.query(models.Account).count()
    return nb_rows, db.query(models.Account).offset(skip).limit(limit).all()


def create_account(db: Session, account: schemas.AccountInit):
    db_item = models.Account(**account.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_account(db: Session, account_id: int, account: schemas.AccountInit, db_item: models.Account):
    for key, val in account.dict().items():
        setattr(db_item, key, val)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_account(db: Session, account_id: int, db_item: models.Account):
    db.delete(db_item)
    db.commit()
    return {'result': f'Account {account_id} successfully deleted'}


# Malls
def get_mall(db: Session, mall_id: int):
    return db.query(models.Mall).filter(models.Mall.id == mall_id).first()


def get_malls(db: Session, skip: int = 0, limit: int = 100):
    nb_rows = db.query(models.Mall).count()
    return nb_rows, db.query(models.Mall).offset(skip).limit(limit).all()


def create_mall(db: Session, mall: schemas.MallCreate):
    db_item = models.Mall(**mall.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_mall(db: Session, mall_id: int, mall: schemas.MallCreate, db_item: models.Mall):
    for key, val in mall.dict().items():
        setattr(db_item, key, val)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_mall(db: Session, mall_id: int, db_item: models.Mall):
    db.delete(db_item)
    db.commit()
    return {'result': f'Mall {mall_id} successfully deleted'}


# Units
def get_unit(db: Session, unit_id: int):
    return db.query(models.Unit).filter(models.Unit.id == unit_id).first()


def get_units(db: Session, skip: int = 0, limit: int = 100):
    nb_rows = db.query(models.Unit).count()
    return nb_rows, db.query(models.Unit).offset(skip).limit(limit).all()


def create_unit(db: Session, unit: schemas.UnitCreate):
    db_item = models.Unit(**unit.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_unit(db: Session, unit_id: int, unit: schemas.UnitCreate, db_item: models.Unit):
    for key, val in unit.dict().items():
        setattr(db_item, key, val)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_unit(db: Session, unit_id: int, db_item: models.Unit):
    db.delete(db_item)
    db.commit()
    return {'result': f'Unit {unit_id} successfully deleted'}
