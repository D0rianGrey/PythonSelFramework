import pytest


@pytest.fixture()
def setup():
    print("I will be executed first")


def test_first_program_Cart3(setup):
    print("I will be executed after SETUP ")
