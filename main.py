
# Press the green button in the gutter to run the script.

from fraction import Fraction


if __name__ == '__main__':
    fragment1 = Fraction(1, 2)
    fragment2 = Fraction(1, 2)
    print(fragment1.__add__(fragment2))
    print(fragment1.__mul__(fragment2))
    print(fragment1 == fragment2)
