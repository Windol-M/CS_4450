# Generated from Q2.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,2,19,6,-1,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,3,0,11,8,0,1,1,
        1,1,1,1,1,1,1,1,3,1,18,8,1,0,0,2,1,1,3,2,1,0,0,20,0,1,1,0,0,0,0,
        3,1,0,0,0,1,10,1,0,0,0,3,17,1,0,0,0,5,6,5,48,0,0,6,7,3,1,0,0,7,8,
        5,48,0,0,8,11,1,0,0,0,9,11,3,3,1,0,10,5,1,0,0,0,10,9,1,0,0,0,11,
        2,1,0,0,0,12,13,5,49,0,0,13,14,3,3,1,0,14,15,5,48,0,0,15,18,1,0,
        0,0,16,18,1,0,0,0,17,12,1,0,0,0,17,16,1,0,0,0,18,4,1,0,0,0,3,0,10,
        17,0
    ]

class Q2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    A = 1
    B = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "A", "B" ]

    ruleNames = [ "A", "B" ]

    grammarFileName = "Q2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


