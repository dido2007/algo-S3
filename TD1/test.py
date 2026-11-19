# -*- coding: utf-8 -*-
from chains import *

def test_powers(name, func, indent=3):
    if func(1,0) is None:
        print(f"skipping '{name}' (unimplemeneted)")
        return
    text_indent = "\t" * indent
    print(f"testing '{name}'...{text_indent}", end="")
    p2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    p3 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147]
    for i in range(len(p2)):
        res = func(2, i)
        if res != p2[i]:
            print(f"wrong value for 2^{i}: should be {p2[i]} but is {res}")
            return
    for i in range(len(p3)):
        res = func(3, i)
        if res != p3[i]:
            print(f"wrong value for 3^{i}: should be {p3[i]} but is {res}")
            return
    print("[ok]")

def test_costs(name, func, expected, indent=2):
    if func(1) is None:
        print(f"skipping '{name}' (unimplemeneted)")
        return
    text_indent = "\t" * indent
    print(f"testing '{name}'...{text_indent}", end="")
    for i in range(len(expected)):
        tmp = func(i)
        if tmp != expected[i]:
            print(f"wrong cost for power {i}: should be {expected[i]} but is {tmp}")
            return
    print("[ok]")

def test1():
    test_powers("bin_power", bin_pow)

def test2():
    test_costs("cost_bin_pow", cost_bin_pow, [0, 0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8, 5, 6, 6, 7, 6, 7, 7, 8, 6, 7, 7, 8, 7, 8, 8, 9, 6, 7])

def test3():
    if smallest_factor(3) is None:
        print("skipping 'smallest_factor' (unimplemeneted)")
        return
    print(f"testing 'smallest_factor'...\t\t", end="")
    ll = [(2, -1), (3, -1), (4, 2), (5, -1), (9, 3), (31, -1), (1001, 7), (100000007, -1), (10007*10007, 10007)]
    for (number, factor) in ll:
        res = smallest_factor(number)
        if res != factor:
            print(f"wrong factor for {number}: should be {factor} but is {res}")
            return
    print("[ok]")

def test4():
    test_powers("factor_pow", factor_pow)

def test5():
    test_costs("cost_factor_pow", cost_factor_pow, [0, 0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 5, 4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 6, 6, 7, 6, 7, 5, 7, 6, 7, 6, 7, 7, 7, 6, 7, 7, 8, 7, 7, 8, 9, 6, 8])

def test6():
    res = power_from_chain(2, [1, 2, 3, 6, 12, 15])
    if res is None:
        print("skipping 'power_from_chain' (unimplemeneted)")
        return
    print("testing 'power_from_chain'...\t\t", end="")
    expected = 32768
    if res != expected:
        print(f"wrong value for 'power_from_chain': should be {expected} but is {res}")
    else:
        print("[ok]")

def test8():
    test_powers("power_tree_pow", power_tree_pow, 2)

def test9():
    test_costs("cost_power_tree_pow", cost_power_tree_pow, [0, 0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 5, 4, 5, 5, 6, 5, 6, 6, 6, 5, 6, 6, 6, 6, 7, 6, 7, 5, 6, 6, 7, 6, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 8, 6, 7], 1)

test1()
test2()
test3()
test4()
test5()
test6()
test8()
test9()
