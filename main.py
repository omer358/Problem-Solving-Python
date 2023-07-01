# Press the green button in the gutter to run the script.

def sum_of_n(n):
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = i + the_sum
    return the_sum


if __name__ == '__main__':
    print(sum_of_n(5))


