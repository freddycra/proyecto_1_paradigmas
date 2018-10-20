
import re
from Rule import Rule
from Grammar import Grammar

#vars {<lista-variables>};
pat_vars = r'^#vars (.*)$'

#symbols {<lista-simbolos>};
pat_symbols = r'^#symbols (.*)'

#markers {<lista-marcadores>};
pat_markers = r'^#markers (.*)'

#basic Pattern match any rule
pat = r'(([a-zA-Z_](\d|\w)*):)?\s?(".*"|.*)\s?(→|->)\s?(".*"|.*)\s?(\(([a-zA-Z_](\d|\w)*)\))?'
# patter for rules with double quotes    "(.*)"\s?(→|->)\s?(.*)
#match rules with labels (non terminal)
pat2 = r'^(\D.*:)?\s?(.*)(→|->)(.*)(\(\D.*\))$'

patLabelI = r'^([a-zA-Z_](\d|\w)*):'
patLabelO = r'\(([a-zA-Z_](\d|\w)*)\)$'

'''
This is the method that checks the sintaxis
of the input string. These are the steps:
1. Takes all the entry and takes out all comments
'''
def checkInput(entry):
    entry = flushComments(entry)
    vars = getVars(entry)
    markers = getMarkers(entry)
    symbols = getSymbols(entry)
    if symbols and not verifySymbols(symbols):
        #raise SyntaxError('Not points allowed in symbols')
        print('Not points allowed in symbols')
    if markers and not verifyMarkers(markers, symbols):
        #raise SyntaxError('Markers can not be symbols')
        print('Markers can not be symbols')
    if not checkLabels(entry):
        #raise SyntaxError('Error in labels')
        print('Error in labels')
    rules = rulesProcessing(entry)
    return createGrammar(rules, symbols, markers, vars)

'''
Perdon por este metodo, esta horrible, pero no
supe como hacerlo de otra forma
lo que hace es devolver la gramatica segun lo que se haya definido
'''
def createGrammar(rules, symbols, markers, vars):
    if not rules:
        print('No rules defined')
        raise Exception('No rules defined')
    if not markers and not vars and not symbols:
        return Grammar(rules)
    if symbols and not vars and not markers:
        return Grammar(rules, symbols)
    if symbols and markers  and not vars:
        return Grammar(rules, symbols, markers)
    if symbols and markers and vars:
        return Grammar(rules, symbols, markers, vars)
    if not symbols and markers and not vars:
        return Grammar(rules, 'abcdefghijklmnopqrstuvwxyz0123456789',\
        markers)
    if not symbols and markers and vars:
        return Grammar(rules, 'abcdefghijklmnopqrstuvwxyz0123456789',\
        markers, vars)
    if not symbols and not markers and vars:
        return Grammar(rules, 'abcdefghijklmnopqrstuvwxyz0123456789',\
        [u'\u03b1',u'\u03b2',u'\u03b3',u'\u03b4'])
    if not markers and symbols and vars:
        return Grammar(rules, symbols, [u'\u03b1',u'\u03b2',u'\u03b3',u'\u03b4'],\
         vars)
    raise Exception('No grammar type concidence')

def rulesProcessing(rules):
    validRules = []
    for i in rules:
        try:
            f = re.search(pat, i)
            spat = spacesChecking(f.group(4))
            rpat = spacesChecking(f.group(6))
            ilab = f.group(1)
            olab = f.group(7)
            validRules.append( Rule(spat, rpat, rpat.endswith('.'), ilab, olab) )
        except SyntaxError:
            print('devolver error a la pantalla')
        except:
            continue
    return validRules


def spacesChecking(line):
    if not spaces(line):
        return delEnclChar(line) if enclosed(line, '"') else line
    elif enclosed(line, '"'):
        return delEnclChar(line)
    elif validSpaces(line):
        return delValidSpaces(line)
    else:
        raise SyntaxError('Error in spaces')


'''
checks if the string is
enclosed in specific charcter
'''
def enclosed(line, c):
    return line.startswith(c) and line.endswith(c)

'''
check if there is any space in
a string
'''
def spaces(line):
    return re.search(r'\s', line) is not None

'''
checks if the spaces is preceded
with \
'''
def validSpaces(line):
    return re.search(r'\\\s', line) is not None

'''
deletes the char that encloses
the string
'''
def delEnclChar(line, spaces=1):
    return line[spaces:-spaces]

'''
Deletes all backslaces after spaces
'''
def delValidSpaces(line):
    return re.sub(r'\\\s', ' ', line)


'''
checks if there is a point in symbols
'''
def verifySymbols(symbols):
    return '.' not in symbols

'''
Verify if there is a marker in symbols
'''
def verifyMarkers(markers, symbols):
    for i in markers:
        if i in symbols:
            return False
    return True

'''
recibes a list with all entry
returns a list without comments
''''
def flushComments(entry):
    return list(filter (lambda x: re.match(r'^[^%].*', x), entry))

'''
returns a list of variables
'''
def getVars(entry):
    var = []
    for i in entry:
        try:
            var.append(re.search(r'^#vars (.*)$', i)[1])
        except:
            continue
    return var if var else []

'''
Return a list with markers if there is
more than one definition, just takes the
firs definition
'''
def getMarkers(entry):
    mar = []
    for i in entry:
        try:
            mar.append(re.search(r'^#markers (.*)', i)[1])
        except:
            continue
    return list(mar[0]) if mar else []

'''
Return a list with the symbols if there is
more than one definition, just takes the
firs definition
'''
def getSymbols(entry):
    sym = ''
    for i in entry:
        try:
            sym = sym + re.search(r'^#symbols (.*)', i)[1]
        except:
            continue
    return sym


'''
Verify if input and output labels
are correct.
'''
def checkLabels(rules):
    temp1 = []
    temp = set()
    for i in rules:
        if re.search(patLabelO, i) is not None:
            temp.add(re.search(patLabelO, i)[1])
    if temp:
        for i in rules:
            if re.search(patLabelI, i) is not None:
                try:
                    temp1.append(re.search(patLabelI, i)[1])
                    temp.remove(re.search(patLabelI, i)[1])
                except:
                    continue
    return len(temp) == 0 and len(temp1) == len(set(temp1))
