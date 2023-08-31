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


def matches(open_s, close_s):
    opens = "({["
    closes = ")}]"
    return opens.index(open_s) == closes.index(close_s)


def par_checker_diff_symbols(symbol_string):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "({[":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and stack.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    # par_checker function for pretenses
    # print(par_checker("((()(())))"))

    # par_checker function for different symbols
    print(par_checker_diff_symbols("[{{([][])}()}]"))
    print(par_checker_diff_symbols("[{()]"))
