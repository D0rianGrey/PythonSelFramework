import pytest


@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


def test_first_program_Cart3(setup):
    print("I will be executed after SETUP ")