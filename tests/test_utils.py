import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import app.utils


# Using the shared fixture
def test_sample_data(sample_data):
    assert len(sample_data) == 5
    assert sample_data == [1, 2, 3, 4, 5]


# Using the setup_database fixture
def test_database_setup(setup_database):
    db = setup_database
    db["users"].append("Alice")
    assert len(db["users"]) == 1
    assert db["users"][0] == "Alice"


# Marking a test as slow
@pytest.mark.slow
def test_slow_function():
    import time

    time.sleep(2)  # Simulate a slow function
    assert True  # Just a placeholder assertion


# Parameterized test
@pytest.mark.parametrize(
    "input_data, expected",
    [
        (1, 2),
        (2, 3),
        (3, 4),
    ],
)
def test_increment(input_data, expected):
    assert input_data + 1 == expected


# Marking a test as a regression test
@pytest.mark.regression
def test_regression_feature():
    assert 1 + 1 == 2  # This should pass


# Marking a test that is expected to fail
@pytest.mark.xfail(reason="This test is expected to fail")
def test_expected_failure():
    assert 1 + 1 == 3  # This will fail


# Another test that is expected to fail
@pytest.mark.xfail(reason="This test is also expected to fail")
def test_another_expected_failure():
    assert "hello" == "world"  # This will also fail


# Example of monkeypatching
def test_fetch_data(monkeypatch):
    def mock_fetch_data():
        return {"data": "mock data"}

    monkeypatch.setattr("app.utils.fetch_data_from_api", mock_fetch_data)
    result = app.utils.fetch_data_from_api()
    assert result == {"data": "mock data"}


@pytest.mark.temporary
def test_temp_file(tmp_path):
    temp_file = tmp_path / "temp_file.txt"
    app.utils.write_to_file(temp_file, "Hello, World!")
    content = app.utils.read_from_file(temp_file)
    assert content == "Hello, World!"
