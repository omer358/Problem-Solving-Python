from basic_data_structure.stack import Stack


def par_checker(symbol_string):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        index = index + 1

    if balanced and stack.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    print(par_checker("((()(())))"))
