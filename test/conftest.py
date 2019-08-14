import pytest

@pytest.fixture(scope="session")
def session_fixture():
    print("It is session fixture")
    yield
    print("Finalizer from session fixture")

@pytest.fixture(scope="module")
def module_fixture(request):
    print("It is module fixture")
    def fin():
        print("Finilizer from module fixture")

    request.addfinalizer(fin)

@pytest.fixture()
def function_fixture():
    print("It is function fixture")