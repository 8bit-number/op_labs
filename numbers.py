

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
        self.args = [x for x in self.args if x not in self.odds]
        self.odds = []

    def clearedOdds(self):
        return A(*self.evens)

    def __str__(self):
        return '{}(evens={},odds={})'.format(self.__class__.__name__, self.evens, self.odds)

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
    def __init__(self, num1, num2):
        super().__init__(*[i for i in range(num1, num2+1)])
        self.num1 = num1
        self.num2 = num2

    def shifted(self, num):
        return B(self.num1+ num, self.num2+num)

    def __str__(self):
        return '{}(evens={},odds={})'.format(self.__class__.__name__, self.evens, self.odds)

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

