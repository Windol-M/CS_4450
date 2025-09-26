# Generated from Q3.g4 by ANTLR 4.13.2
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
        4,1,2,36,2,0,7,0,1,0,5,0,4,8,0,10,0,12,0,7,9,0,1,0,5,0,10,8,0,10,
        0,12,0,13,9,0,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,1,0,5,0,24,
        8,0,10,0,12,0,27,9,0,5,0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,1,0,0,0,
        1,0,0,0,39,0,5,1,0,0,0,2,4,5,1,0,0,3,2,1,0,0,0,4,7,1,0,0,0,5,3,1,
        0,0,0,5,6,1,0,0,0,6,30,1,0,0,0,7,5,1,0,0,0,8,10,5,1,0,0,9,8,1,0,
        0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,
        1,0,0,0,14,18,5,2,0,0,15,17,5,1,0,0,16,15,1,0,0,0,17,20,1,0,0,0,
        18,16,1,0,0,0,18,19,1,0,0,0,19,21,1,0,0,0,20,18,1,0,0,0,21,25,5,
        2,0,0,22,24,5,1,0,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,
        26,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,28,11,1,0,0,0,29,32,1,0,0,
        0,30,28,1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,
        5,0,0,1,34,1,1,0,0,0,5,5,11,18,25,30
    ]

class Q3Parser ( Parser ):

    grammarFileName = "Q3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'0'", "'1'" ]

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

        def EOF(self):
            return self.getToken(Q3Parser.EOF, 0)

        def A(self, i:int=None):
            if i is None:
                return self.getTokens(Q3Parser.A)
            else:
                return self.getToken(Q3Parser.A, i)

        def B(self, i:int=None):
            if i is None:
                return self.getTokens(Q3Parser.B)
            else:
                return self.getToken(Q3Parser.B, i)

        def getRuleIndex(self):
            return Q3Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = Q3Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2
                    self.match(Q3Parser.A) 
                self.state = 7
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 8
                    self.match(Q3Parser.A)
                    self.state = 13
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 14
                self.match(Q3Parser.B)
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 15
                    self.match(Q3Parser.A)
                    self.state = 20
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 21
                self.match(Q3Parser.B)
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 22
                        self.match(Q3Parser.A) 
                    self.state = 27
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(Q3Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





