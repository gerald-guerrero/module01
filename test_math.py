import pytest

@pytest.fixture
def sample_data():
    """
    A fixture that provides a list of sample data.
    """
    return [1, 2, 3, 4, 5]

def test_sample_data_length(sample_data):
    """
    This test checks that the length of the sample is 3.
    """
    assert len(sample_data) == 3

def test_sample_data_values(sample_data):
    """
    This test checks that the sample data matches the expected list.
    """
    assert sample_data == [1, 2, 3]
