
class Grammar(object):
    def __init__(self):
        super(Grammar, self).__init__()
        self.rules = []

    def addRule(self, rule):
        if self.checkRule(rule):
            self.rules.append(rule)

    def checkRule(self, rule):
        return rule is not None;

    def printInfo(self):
        print(self.rules)
