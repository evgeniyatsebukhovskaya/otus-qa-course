import pytest


def test_lenght_of_list(session_fixture, module_fixture, function_fixture):
    """Проверяем, что функция len возвращает длину списка"""
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    lenth_of_list = len(list)
    if lenth_of_list == 8:
        print("test N1 is passed")


def test_summ_of_two_strings(session_fixture, module_fixture, function_fixture):
    """Проверяем, что оператор + складывает 2 строки"""
    str1 = 'stro'
    str2 = 'ka'
    str = str1+str2
    if str == 'stroka':
        print("test N2 is passed")


def test_multiply_number_to_string(session_fixture, module_fixture, function_fixture):
    """Проверяем. что оператор * умножает строку на заданное число"""
    str = 'abc'
    multiplied_str = 3*str
    if multiplied_str == 'abcabcabc':
        print("test N3 is passed")


def test_clear_of_list(session_fixture, module_fixture, function_fixture):
    """Проверяем, что функция clear отчищает список"""
    list = ['aa', 'bb', 'cc']
    list.clear()
    if len(list) == 0:
        print("test N4 is passed")


def test_ammount_of_x_in_list(session_fixture, module_fixture, function_fixture):
    """Проверяем, что функция count находит число вхождений в список"""
    list = ['qq', 'x', 'aaz', 'x']
    ammount = list.count('x')
    if ammount == 2:
        print("test N5 is passed")


def test_reversed_list(session_fixture, module_fixture, function_fixture):
    """Проверяем, что функция reverse переворачивает список"""
    list = ['first one', 'middle one', 'last one']
    list.reverse()
    first_of_reversed = list[0]
    if first_of_reversed == 'last one':
        print("test N6 is passed")


def test_set_consist_of_unique_elements(session_fixture, module_fixture, function_fixture):
    """Проверяем. что множество содержит только уникальные элементы"""
    s = set()
    s.add(1)
    s.add(2)
    s.add(1)
    lenth = len(s)
    if lenth == 2:
        print("test N7 is passed")


def test_getting_dictionary_value_by_key(session_fixture, module_fixture, function_fixture):
    """Проверяем, что по ключу можно получить значение из словаря"""
    d = dict(key1='value1', key2='value2', key3='value3')
    if d['key1'] == 'value1':
        print("test N8 is passed")


def test_switch_values(session_fixture, module_fixture, function_fixture):
    """Проверяем, что значения переменных поменены"""
    a = 5
    b = 10
    a, b = b, a
    if a == 10:
        print("test N9 is passed")


def test_insert_value(session_fixture, module_fixture, function_fixture):
    """Проверяем, что функция insert вставляет значение в список"""
    l = ['first one', 'middle one', 'last one']
    l.insert(0, 'new first one')
    if l[0] == 'new first one':
        print("test N10 is passed")

