class Another:
    def __init__(self, x):
        self.a = x
        self.count = 0

    def __str__(self):
        return "{}, {}".format(len(self.a), sum(self.a))

    def twiddle(self):
        self.count += 1
        self.a.append(self.count)

def sigh(x):
    x.twiddle()
    x.twiddle()
    x.twiddle()
    print(x)

sigh(Another([1,992,1]))