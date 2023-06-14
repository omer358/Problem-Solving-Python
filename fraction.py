class Fragment:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        # print the fraction in the form a/b
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other_fraction: Fragment):
        new_num = self.num*other_fraction.den
