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


def test_lenght_of_list(session_fixture, module_fixture, function_fixture):
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    lenth_of_list = len(list)
    if(lenth_of_list == 8):
        pass

def test_summ_of_two_strings(session_fixture, module_fixture, function_fixture):
    str1 = 'stro'
    str2 = 'ka'
    str = str1+str2
    if(str == 'stroka'):
        pass

def test_multiply_number_to_string(session_fixture, module_fixture, function_fixture):
    str = 'abc'
    multiplied_str = 3*str
    if(multiplied_str == 'abcabcabc'):
        pass

def test_clear_of_list(session_fixture, module_fixture, function_fixture):
    list = ['aa', 'bb', 'cc']
    list.clear()
    if(len(list) == 0):
        pass

def test_ammount_of_x_in_list(session_fixture, module_fixture, function_fixture):
    list = ['qq', 'x', 'aaz', 'x']
    ammount = list.count('x')
    print(ammount)
    if(ammount == 2):
        pass

def test_reversed_list(session_fixture, module_fixture, function_fixture):
    list = ['first one', 'middle one', 'last one']
    list.reverse()
    first_of_reversed = list[0]
    print(first_of_reversed)
    if(first_of_reversed == 'last one'):
        pass

def test_set_consist_of_unique_elements(session_fixture, module_fixture, function_fixture):
    s = set()
    s.add(1)
    s.add(2)
    s.add(1)
    lenth = len(s)
    print(lenth)
    if(lenth == 2):
        pass

def test_getting_dictionary_value_by_key(session_fixture, module_fixture, function_fixture):
    d = dict(key1='value1', key2='value2', key3='value3')
    if d['key1'] == 'value':
        print("test is passed")
