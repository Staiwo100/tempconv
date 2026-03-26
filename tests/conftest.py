import pytest


@pytest.fixture
def freezing_point():
    return {"C": 0.0, "F": 32.0, "K": 273.15}


@pytest.fixture
def boiling_point():
    return {"C": 100.0, "F": 212.0, "K": 373.15}
