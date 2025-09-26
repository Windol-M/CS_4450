# Generated from Q4.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,22,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,3,1,15,8,1,1,2,5,2,18,8,2,10,2,12,2,21,9,2,0,0,3,1,1,3,2,5,3,1,
        0,0,23,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,1,7,1,0,0,0,3,14,1,0,
        0,0,5,19,1,0,0,0,7,8,5,97,0,0,8,2,1,0,0,0,9,10,5,97,0,0,10,11,3,
        3,1,0,11,12,5,97,0,0,12,15,1,0,0,0,13,15,3,5,2,0,14,9,1,0,0,0,14,
        13,1,0,0,0,15,4,1,0,0,0,16,18,5,98,0,0,17,16,1,0,0,0,18,21,1,0,0,
        0,19,17,1,0,0,0,19,20,1,0,0,0,20,6,1,0,0,0,21,19,1,0,0,0,3,0,14,
        19,0
    ]

class Q4Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    A = 2
    B = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'a'" ]

    symbolicNames = [ "<INVALID>",
            "A", "B" ]

    ruleNames = [ "T__0", "A", "B" ]

    grammarFileName = "Q4.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


