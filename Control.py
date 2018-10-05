from Model import Model

class Control(object):
    def __init__(self):
        super(Control, self).__init__()
        self.model = Model()

    def addRules(self, rules):
        self.model.addRules(rules)

    def printInfo(self):
        self.model.printInfo()
