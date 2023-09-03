from basic_data_structure.stack import Stack

"""Takes a decimal number and any base between 2 and 16 as parameters"""


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


if __name__ == "__main__":
    print(base_converter(233, 16))
