# Press the green button in the gutter to run the script.
import time
import timeit

from timeit import Timer
from anagram_detection import *


def sum_of_n(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = i + the_sum
        end = time.time()
    return the_sum, end - start


def sum_of_n2(n):
    stat = time.time()
    the_sum = (n * (n + 1)) / 2
    end = time.time()
    return the_sum, end - stat


if __name__ == '__main__':
    t1 = Timer("test1()", "from performance_data_structure.lists_performance import test1")
    print("Concat", t1.timeit(number=100), "milliseconds")
    t2 = Timer("test2()", "from performance_data_structure.lists_performance import test2")
    print("append", t2.timeit(number=100), "milliseconds")
    t3 = Timer("test3()", "from performance_data_structure.lists_performance import test3")
    print("comprehension", t3.timeit(number=100), "milliseconds")
    t4 = Timer("test4()", "from performance_data_structure.lists_performance import test4")
    print("List range", t4.timeit(number=100), "milliseconds")
