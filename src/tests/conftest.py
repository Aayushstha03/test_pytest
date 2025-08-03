# conftest.py
import pytest


@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def setup_database():
    # Simulate setting up a database connection
    db = {"users": []}
    yield db
    # Simulate tearing down the database connection
    db.clear()
