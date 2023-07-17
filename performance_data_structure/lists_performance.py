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
