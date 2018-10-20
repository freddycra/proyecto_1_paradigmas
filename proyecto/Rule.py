
class Rule(object):
    def __init__(self, pattern, substitution, final=False, ilabel=None, olabel=None):
        super(Rule, self).__init__()
        self.pattern = pattern
        self.substitution = substitutio
        self.ilabel = ilabel
        self.olabel = olabel

    def printRule(self):
        print(self.ilabel, " ", self.pattern, " -> ", self.substitution, " ", self.olabel)
