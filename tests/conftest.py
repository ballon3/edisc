import pytest
from fastapi_utils.db.mongoengine import connect_to_mongoengine
from starlette.testclient import TestClient

from src.app.main import app


@pytest.fixture(scope="module")
def client():
    client = TestClient(app)
    connect_to_mongoengine()
    yield client


@pytest.fixture(scope="module")
def prefix():
    # TODO read this in from main.py or something
    return "/api/sauth/v2"
