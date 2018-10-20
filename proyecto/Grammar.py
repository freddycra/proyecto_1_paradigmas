
class Grammar(object):
    def __init__(self, rules, symbols = 'abcdefghijklmnopqrstuvwxyz0123456789',\
    markers=[u'\u03b1',u'\u03b2',u'\u03b3',u'\u03b4'], vars = 'xywz'):
        super(Grammar, self).__init__()
        self.rules = rules
        self.markers = markers
        self.symbols = symbols
        self.vars = vars

    def printInfo(self):
        print(self.rules)
