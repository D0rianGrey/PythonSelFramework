import pytest


@pytest.fixture(scope="class")
def setup():
    # setUp
    print("I will be executed first BEFORE EVERY CASE")
    yield
    # teardown
    print("I will be executed last AFTER EVERY CASE")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["First_Value", "Second_Value", "Third_Value"]


@pytest.fixture(params=["chrome", "firefox", "ie"])
def crossBrowser(request):
    return request.param
