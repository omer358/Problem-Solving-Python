# Press the green button in the gutter to run the script.
import time


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
    return the_sum, end -stat

    
if __name__ == '__main__':
    for i in range(5):
        print("Sum is %d required %10.7f seconds" % sum_of_n2(10000))
