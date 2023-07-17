import pytest
from httpx import Client
from starlette.testclient import TestClient

from delvify.main import ms
from delvify.schemas import Email


@pytest.fixture()
def client() -> Client:
    return TestClient(ms)


@pytest.fixture
def test_email() -> Email:
    return Email(destination="example@example.com", subject="My subject", body="My body")
