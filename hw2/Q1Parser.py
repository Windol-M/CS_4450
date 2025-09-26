# Generated from Q1.g4 by ANTLR 4.13.2
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
        4,1,2,25,2,0,7,0,1,0,5,0,4,8,0,10,0,12,0,7,9,0,1,0,1,0,5,0,11,8,
        0,10,0,12,0,14,9,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,
        0,0,0,1,0,0,0,26,0,5,1,0,0,0,2,4,5,2,0,0,3,2,1,0,0,0,4,7,1,0,0,0,
        5,3,1,0,0,0,5,6,1,0,0,0,6,8,1,0,0,0,7,5,1,0,0,0,8,12,5,1,0,0,9,11,
        5,2,0,0,10,9,1,0,0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,
        15,1,0,0,0,14,12,1,0,0,0,15,19,5,1,0,0,16,18,5,2,0,0,17,16,1,0,0,
        0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,
        1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,3,5,12,19
    ]

class Q1Parser ( Parser ):

    grammarFileName = "Q1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'" ]

    symbolicNames = [ "<INVALID>", "A", "B" ]

    RULE_start = 0

    ruleNames =  [ "start" ]

    EOF = Token.EOF
    A=1
    B=2

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

        def A(self, i:int=None):
            if i is None:
                return self.getTokens(Q1Parser.A)
            else:
                return self.getToken(Q1Parser.A, i)

        def EOF(self):
            return self.getToken(Q1Parser.EOF, 0)

        def B(self, i:int=None):
            if i is None:
                return self.getTokens(Q1Parser.B)
            else:
                return self.getToken(Q1Parser.B, i)

        def getRuleIndex(self):
            return Q1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = Q1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 2
                self.match(Q1Parser.B)
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 8
            self.match(Q1Parser.A)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 9
                self.match(Q1Parser.B)
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self.match(Q1Parser.A)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 16
                self.match(Q1Parser.B)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(Q1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





