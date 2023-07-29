from timeit import Timer


def test1():
    my_list = []
    for i in range(1000):
        my_list = my_list + [i]


def test2():
    my_list = []
    for i in range(1000):
        my_list.append(i)


def test3():
    my_list = [i for i in range(1000)]


def test4():
    my_list = list(range(1000))


if __name__ == '__main__':
    # pop_end = Timer("x.pop()", "from __main__ import x")
    # pop_zero = Timer("x.pop(0)", "from __main__ import x")
    #
    # x = list(range(2000000))
    # print(pop_zero.timeit(number=1000))
    #
    # x = list(range(2000000))
    # print(pop_end.timeit(number=1000))

    # pop operations on a different size of lists
    pop_end = Timer("x.pop()", "from __main__ import x")
    pop_zero = Timer("x.pop(0)", "from __main__ import x")
    print("\tpop(0)  pop()")
    for i in range(1000000, 10000001, 1000000):
        x = list(range(i))
        pt = pop_end.timeit(number=1000)

        x = list(range(i))
        pz = pop_zero.timeit(number=1000)
        print("%15.5f, %15.5f" %(pz,pt))
