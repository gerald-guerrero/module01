import pytest 

@pytest.fixture
def some_data():
    # Setup code goes here (creating test data, database connections, etc.)
    return 42

def test_example(some_data):
    # Use the fixture value in your test
    assert some_data == 42