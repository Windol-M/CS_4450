# Generated from Q4.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,8,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,6,0,2,1,0,0,
        0,2,3,5,1,0,0,3,4,5,2,0,0,4,5,5,1,0,0,5,6,5,0,0,1,6,1,1,0,0,0,0
    ]

class Q4Parser ( Parser ):

    grammarFileName = "Q4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "A", "B" ]

    RULE_start = 0

    ruleNames =  [ "start" ]

    EOF = Token.EOF
    T__0=1
    A=2
    B=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def A(self):
            return self.getToken(Q4Parser.A, 0)

        def EOF(self):
            return self.getToken(Q4Parser.EOF, 0)

        def getRuleIndex(self):
            return Q4Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = Q4Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(Q4Parser.T__0)
            self.state = 3
            self.match(Q4Parser.A)
            self.state = 4
            self.match(Q4Parser.T__0)
            self.state = 5
            self.match(Q4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





