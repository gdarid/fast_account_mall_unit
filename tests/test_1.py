from fastapi.testclient import TestClient
from api.main import app, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.database import Base
import os

SQLALCHEMY_DATABASE_PATH = "./test.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///" + SQLALCHEMY_DATABASE_PATH
try:
    os.remove(SQLALCHEMY_DATABASE_PATH)
except FileNotFoundError:
    pass

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = None
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_home():
    response = client.get(
        "/"
    )
    assert response.status_code == 200
    assert "<title>FastAPI - Swagger UI</title>" in response.text


def test_one_account():
    # Create account
    response = client.post(
        "/accounts/",
        json={"name": "The super account"},
    )
    assert response.status_code == 200
    res = response.json()
    assert res["name"] == "The super account"

    # Get account
    response = client.get(
        "/accounts/"
    )
    assert response.status_code == 200
    res = response.json()
    assert res["nb_rows"] == 1

    response = client.get(
        "/accounts/1"
    )
    assert response.status_code == 200
    res = response.json()
    assert res["name"] == "The super account"

    response = client.get(
        "/accounts/1000"
    )
    assert response.status_code == 404

    # Update account
    response = client.put(
        "/accounts/1",
        json={"name": "The new super account"},
    )
    assert response.status_code == 200
    res = response.json()
    assert res["name"] == "The new super account"

    response = client.put(
        "/accounts/1000",
        json={"name": "The new super account"},
    )
    assert response.status_code == 404

    # Delete account
    response = client.delete(
        "/accounts/1",
    )
    assert response.status_code == 200

    res = response.json()
    assert res['result'].endswith(' successfully deleted')

    response = client.delete(
        "/accounts/1000",
    )
    assert response.status_code == 404


def test_one_mall():
    # Create mall
    response = client.post(
        "/malls/",
        json={"name": "The super mall"},
    )
    assert response.status_code == 200
    res = response.json()
    assert res["name"] == "The super mall"

    # Get mall
    response = client.get(
        "/malls/"
    )
    assert response.status_code == 200
    res = response.json()
    assert res["nb_rows"] == 1

    response = client.get(
        "/malls/1"
    )
    assert response.status_code == 200
    res = response.json()
    assert res["name"] == "The super mall"

    response = client.get(
        "/malls/1000"
    )
    assert response.status_code == 404

    # Update mall
    response = client.put(
        "/malls/1",
        json={"name": "The new super mall"},
    )
    assert response.status_code == 200
    res = response.json()
    assert res["name"] == "The new super mall"

    response = client.put(
        "/malls/1000",
        json={"name": "The new super mall"},
    )
    assert response.status_code == 404

    # Delete mall
    response = client.delete(
        "/malls/1",
    )
    assert response.status_code == 200

    res = response.json()
    assert res['result'].endswith(' successfully deleted')

    response = client.delete(
        "/malls/1000",
    )
    assert response.status_code == 404


def test_one_unit():
    # Create unit
    response = client.post(
        "/units/",
        json={"name": "The super unit"},
    )
    assert response.status_code == 200
    res = response.json()
    assert res["name"] == "The super unit"

    # Get unit
    response = client.get(
        "/units/"
    )
    assert response.status_code == 200
    res = response.json()
    assert res["nb_rows"] == 1

    response = client.get(
        "/units/1"
    )
    assert response.status_code == 200
    res = response.json()
    assert res["name"] == "The super unit"

    response = client.get(
        "/units/1000"
    )
    assert response.status_code == 404

    # Update unit
    response = client.put(
        "/units/1",
        json={"name": "The new super unit"},
    )
    assert response.status_code == 200
    res = response.json()
    assert res["name"] == "The new super unit"

    response = client.put(
        "/units/1000",
        json={"name": "The new super unit"},
    )
    assert response.status_code == 404

    # Delete unit
    response = client.delete(
        "/units/1",
    )
    assert response.status_code == 200

    res = response.json()
    assert res['result'].endswith(' successfully deleted')

    response = client.delete(
        "/units/1000",
    )
    assert response.status_code == 404
