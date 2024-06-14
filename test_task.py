
from task import calculate_max_profit

def test_case_1():
    assert 0 == calculate_max_profit([], n=5)

def test_case_2():
    assert 0 == calculate_max_profit([-1, -2, -3], n=3)

def test_case_3():
    assert 5 == calculate_max_profit([2, -4, 3, 2, -1], n=3)

def test_case_4():
    assert 10 == calculate_max_profit([-2, 1, 2, 3, 4, -1], n=4)

def test_case_5():
    assert 4 == calculate_max_profit([-1, -1, -2, -3, -4, 4, -5], n=5)
    
def test_case_6():
    assert 13 == calculate_max_profit([1, 4, 3, -1, 9, -2, 6, 2], n=3)

def test_case_7():
    assert 20 == calculate_max_profit([1, 2, 3, 4, 5, -1, -1, 20, -1, 6, 7 , 8], n=2)

def test_case_8():
    assert 0 == calculate_max_profit([1, 2, 3, 4, 5], n=0)

def test_case_9():
    with open('big_input.txt') as f:
        nums = eval(f.read())
    assert 1103103 == calculate_max_profit(nums, n=120)