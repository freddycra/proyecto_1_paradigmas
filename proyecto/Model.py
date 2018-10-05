from Grammar import Grammar

class Model(object):
    def __init__(self):
        super(Model, self).__init__()
        self.grammar = Grammar()

    def addRules(self, rules):
        my_list = rules.split('\n')
        for i in my_list:
            self.grammar.addRule(i)

    def printInfo(self):
        self.grammar.printInfo()
