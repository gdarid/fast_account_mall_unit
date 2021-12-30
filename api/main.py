from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():  # pragma: no cover # The function is not detected by coverage because it is overriden for testing reason
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Home : redirection to /docs
@app.get("/", response_class=RedirectResponse)
async def redirect_fastapi():
    return "/docs"


# Accounts
@app.post("/accounts/", response_model=schemas.Account, tags=["account"])
def create_account(account: schemas.AccountInit, db: Session = Depends(get_db)):
    return crud.create_account(db, account)


@app.get("/accounts/", tags=["account"])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    nb_rows, accounts = crud.get_accounts(db, skip, limit)
    return {"nb_rows": nb_rows, "items": accounts}


@app.get("/accounts/{account_id}", response_model=schemas.Account, tags=["account"])
def read_account(account_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_account(db, account_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=f"Account {account_id} not found")
    return db_item


@app.put("/accounts/{account_id}", response_model=schemas.Account, tags=["account"])
@app.patch("/accounts/{account_id}", response_model=schemas.Account, tags=["account"])
def update_account(account_id: int, account: schemas.AccountInit, db: Session = Depends(get_db)):
    db_item = crud.get_account(db, account_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=f"Account {account_id} not found")
    return crud.update_account(db, account_id, account, db_item)


@app.delete("/accounts/{account_id}", tags=["account"])
def delete_account(account_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_account(db, account_id=account_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=f"Account {account_id} not found")
    return crud.delete_account(db, account_id, db_item)


# Malls
@app.post("/malls/", response_model=schemas.Mall, tags=["mall"])
def create_mall(mall: schemas.MallCreate, db: Session = Depends(get_db)):
    return crud.create_mall(db, mall)


@app.get("/malls/", tags=["mall"])
def read_malls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    nb_rows, malls = crud.get_malls(db, skip, limit)
    return {"nb_rows": nb_rows, "items": malls}


@app.get("/malls/{mall_id}", response_model=schemas.Mall, tags=["mall"])
def read_mall(mall_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_mall(db, mall_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=f"Mall {mall_id} not found")
    return db_item


@app.put("/malls/{mall_id}", response_model=schemas.Mall, tags=["mall"])
@app.patch("/malls/{mall_id}", response_model=schemas.Mall, tags=["mall"])
def update_mall(mall_id: int, mall: schemas.MallCreate, db: Session = Depends(get_db)):
    db_item = crud.get_mall(db, mall_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=f"Mall {mall_id} not found")
    return crud.update_mall(db, mall_id, mall, db_item)


@app.delete("/malls/{mall_id}", tags=["mall"])
def delete_mall(mall_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_mall(db, mall_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=f"Mall {mall_id} not found")
    return crud.delete_mall(db, mall_id, db_item)


# Units
@app.post("/units/", response_model=schemas.Unit, tags=["unit"])
def create_unit(unit: schemas.UnitCreate, db: Session = Depends(get_db)):
    return crud.create_unit(db, unit)


@app.get("/units/", tags=["unit"])
def read_units(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    nb_rows, units = crud.get_units(db, skip, limit)
    return {"nb_rows": nb_rows, "items": units}


@app.get("/units/{unit_id}", response_model=schemas.Unit, tags=["unit"])
def read_unit(unit_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_unit(db, unit_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=f"Unit {unit_id} not found")
    return db_item


@app.put("/units/{unit_id}", response_model=schemas.Unit, tags=["unit"])
@app.patch("/units/{unit_id}", response_model=schemas.Unit, tags=["unit"])
def update_unit(unit_id: int, unit: schemas.UnitCreate, db: Session = Depends(get_db)):
    db_item = crud.get_unit(db, unit_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=f"Unit {unit_id} not found")
    return crud.update_unit(db, unit_id, unit, db_item)


@app.delete("/units/{unit_id}", tags=["unit"])
def delete_unit(unit_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_unit(db, unit_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=f"Unit {unit_id} not found")
    return crud.delete_unit(db, unit_id, db_item)
