class Fragment:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        # print the fraction in the form a/b
        return "{}/{}".format(self.num, self.den)