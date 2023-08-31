from basic_data_structure.stack import Stack


def divide_by_2(dec_number):
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2

    bin_number = ""
    while not rem_stack.is_empty():
        bin_number = bin_number + str(rem_stack.pop())

    return bin_number


if __name__ == "__main__":
    print(divide_by_2(233))
