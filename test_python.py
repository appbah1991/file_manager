import unittest
import math

#filter
seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)
filtered = filter(lambda x: x % 2 == 0, seq)
def test_filter():
    test_list = [2, 4, 6, 8]
    assert list(filtered) == list(test_list)
    print('Функция "filter" работает верно')
test_filter()

#map
seq_map = [2, 4, 6, 8, 10]
maped = map(lambda x: x/2, seq_map)

def test_map():
    test_list_map = [1, 2, 3, 4, 5]
    assert list(maped) == list(test_list_map)
    print('Функция "map" работает верно')
test_map()

#sorted
seq_to_sort = [5, 7, 1, 7, 9, 55, 765, 43]
new_sorted = sorted(seq_to_sort)

def test_sorted():
    test_list_sorted = [1, 5, 7, 7, 9, 43, 55, 765]
    assert list(new_sorted) == list(test_list_sorted)
    print('Функция "sorted" работает верно')
test_sorted()

#pi

def test_pi():
    assert math.pi == 3.141592653589793
    print('Функция "pi" работает верно')
test_pi()

#sqrt
sqrt_1 = int(math.sqrt(16))
sqrt_2 = int(math.sqrt(4))
sqrt_3 = int(math.sqrt(25))
sqrt_4 = int(math.sqrt(81))
def test_sqrt():
    assert sqrt_1 == 4
    assert sqrt_2 == 2
    assert sqrt_3 == 5
    assert sqrt_4 == 9
    print('Функция "sqrt" работает верно')
test_sqrt()

#pow
pow_1 = math.pow(2 ,2)
pow_2 = math.pow(3 ,2)
pow_3 = math.pow(3 ,3)
pow_4 = math.pow(4 ,2)
def test_pow():
    assert pow_1 == 4
    assert pow_2 == 9
    assert pow_3 == 27
    assert pow_4 == 16
    print('Функция "pow" работает верно')
test_pow()

#hypot
hypot_1 = math.hypot(2 ,3)
hypot_2 = math.hypot(3 ,2)
hypot_3 = math.hypot(3 ,3)
hypot_4 = math.hypot(4 ,2)
def test_hypot():
    assert hypot_1 == 3.605551275463989
    assert hypot_2 == 3.605551275463989
    assert hypot_3 == 4.242640687119285
    assert hypot_4 == 4.47213595499958
    print('Функция "hypot" работает верно')
test_hypot()


