from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas


def commit(db: Session, name: str):
    try:
        db.commit()
    except IntegrityError:
        raise ValueError("Integrity error for " + name)


# Accounts
def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()


def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    nb_rows = db.query(models.Account).count()
    return nb_rows, db.query(models.Account).offset(skip).limit(limit).all()


def create_account(db: Session, account: schemas.AccountInit):
    db_item = models.Account(**account.model_dump())
    db.add(db_item)
    commit(db, "account")
    db.refresh(db_item)
    return db_item


def update_account(db: Session, account_id: int, account: schemas.AccountInit, db_item: models.Account):
    for key, val in account.model_dump().items():
        setattr(db_item, key, val)
    commit(db, "account")
    db.refresh(db_item)
    return db_item


def delete_account(db: Session, account_id: int, db_item: models.Account):
    db.delete(db_item)
    commit(db, "account")
    return {'result': f'Account {account_id} successfully deleted'}


# Malls
def get_mall(db: Session, mall_id: int):
    return db.query(models.Mall).filter(models.Mall.id == mall_id).first()


def get_malls(db: Session, skip: int = 0, limit: int = 100):
    nb_rows = db.query(models.Mall).count()
    return nb_rows, db.query(models.Mall).offset(skip).limit(limit).all()


def create_mall(db: Session, mall: schemas.MallInit):
    db_item = models.Mall(**mall.model_dump())
    db.add(db_item)
    commit(db, "mall")
    db.refresh(db_item)
    return db_item


def update_mall(db: Session, mall_id: int, mall: schemas.MallInit, db_item: models.Mall):
    for key, val in mall.model_dump().items():
        setattr(db_item, key, val)
    commit(db, "mall")
    db.refresh(db_item)
    return db_item


def delete_mall(db: Session, mall_id: int, db_item: models.Mall):
    db.delete(db_item)
    commit(db, "mall")
    return {'result': f'Mall {mall_id} successfully deleted'}


# Units
def get_unit(db: Session, unit_id: int):
    return db.query(models.Unit).filter(models.Unit.id == unit_id).first()


def get_units(db: Session, skip: int = 0, limit: int = 100):
    nb_rows = db.query(models.Unit).count()
    return nb_rows, db.query(models.Unit).offset(skip).limit(limit).all()


def create_unit(db: Session, unit: schemas.UnitInit):
    db_item = models.Unit(**unit.model_dump())
    db.add(db_item)
    commit(db, "unit")
    db.refresh(db_item)
    return db_item


def update_unit(db: Session, unit_id: int, unit: schemas.UnitInit, db_item: models.Unit):
    for key, val in unit.model_dump().items():
        setattr(db_item, key, val)
    commit(db, "unit")
    db.refresh(db_item)
    return db_item


def delete_unit(db: Session, unit_id: int, db_item: models.Unit):
    db.delete(db_item)
    commit(db, "unit")
    return {'result': f'Unit {unit_id} successfully deleted'}
