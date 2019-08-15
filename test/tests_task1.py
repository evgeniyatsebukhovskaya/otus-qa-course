import pytest


def test_lenght_of_list(session_fixture, module_fixture, function_fixture):
    """Проверяем, что функция len возвращает длину списка"""
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    lenth_of_list = len(list)
    assert lenth_of_list == 8

def test_summ_of_two_strings(session_fixture, module_fixture, function_fixture):
    """Проверяем, что оператор + складывает 2 строки"""
    str1 = 'stro'
    str2 = 'ka'
    str = str1+str2
    assert str == 'stroka'


def test_multiply_number_to_string(session_fixture, module_fixture, function_fixture):
    """Проверяем. что оператор * умножает строку на заданное число"""
    str = 'abc'
    multiplied_str = 3*str
    assert multiplied_str == 'abcabcabc'


def test_clear_of_list(session_fixture, module_fixture, function_fixture):
    """Проверяем, что функция clear отчищает список"""
    list = ['aa', 'bb', 'cc']
    list.clear()
    assert len(list) == 0


def test_ammount_of_x_in_list(session_fixture, module_fixture, function_fixture):
    """Проверяем, что функция count находит число вхождений в список"""
    list = ['qq', 'x', 'aaz', 'x']
    ammount = list.count('x')
    assert ammount == 2


def test_reversed_list(session_fixture, module_fixture, function_fixture):
    """Проверяем, что функция reverse переворачивает список"""
    list = ['first one', 'middle one', 'last one']
    list.reverse()
    first_of_reversed = list[0]
    assert first_of_reversed == 'last one'

def test_set_consist_of_unique_elements(session_fixture, module_fixture, function_fixture):
    """Проверяем. что множество содержит только уникальные элементы"""
    s = set()
    s.add(1)
    s.add(2)
    s.add(1)
    lenth = len(s)
    assert lenth == 2


def test_getting_dictionary_value_by_key(session_fixture, module_fixture, function_fixture):
    """Проверяем, что по ключу можно получить значение из словаря"""
    d = dict(key1='value1', key2='value2', key3='value3')
    assert d['key1'] == 'value1'


def test_switch_values(session_fixture, module_fixture, function_fixture):
    """Проверяем, что значения переменных поменены"""
    a = 5
    b = 10
    a, b = b, a
    assert a == 10


def test_insert_value(session_fixture, module_fixture, function_fixture):
    """Проверяем, что функция insert вставляет значение в список"""
    l = ['first one', 'middle one', 'last one']
    l.insert(0, 'new first one')
    assert l[0] == 'new first one'

