class A:
    def __init__(self, *args):
        self.args = list(args)
        self.evens = []
        self.odds = []
        for i in args:
            if i % 2 == 0:
                self.evens.append(i)
            else:
                self.odds.append(i)
        self.evens.sort()

    def clearOdds(self):
        self.somelist = [x for x in self.args if x not in self.odds]

    def clearedOdds(self):
        self.args = [x for x in self.args if x not in self.odds]

        return self.args


    def __str__(self):
        return 'A(evens={},odds={})'.format(self.evens, self.odds)

    def __eq__(self, other):
        try:
            if self.evens == other.evens:
                return True
            return False
        except AttributeError:
            return False

    def __ne__(self, other):
        try:
            if self.evens != other.evens:
                return True
        except AttributeError:
            return True

class B(A):
    def __init__(self, *args):
        super().__init__(*args)

    def shifted(self, num):
        self.num = num
        for i in range(len(self.args)):
            self.args[i] = self.args[i] + self.num
