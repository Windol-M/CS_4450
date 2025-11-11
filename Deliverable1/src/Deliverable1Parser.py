# Generated from grammar/Deliverable1.g4 by ANTLR 4.13.1
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
        4,1,23,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,3,0,21,8,0,5,0,23,8,0,10,0,12,0,26,9,0,
        1,0,1,0,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,5,
        4,43,8,4,10,4,12,4,46,9,4,1,5,1,5,1,5,5,5,51,8,5,10,5,12,5,54,9,
        5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,67,8,7,1,7,1,7,
        1,7,1,7,1,7,3,7,74,8,7,1,8,1,8,1,8,1,8,5,8,80,8,8,10,8,12,8,83,9,
        8,3,8,85,8,8,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,1,5,
        1,0,6,7,1,0,8,10,93,0,24,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,37,
        1,0,0,0,8,39,1,0,0,0,10,47,1,0,0,0,12,55,1,0,0,0,14,73,1,0,0,0,16,
        75,1,0,0,0,18,20,3,2,1,0,19,21,5,21,0,0,20,19,1,0,0,0,20,21,1,0,
        0,0,21,23,1,0,0,0,22,18,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,
        1,0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,
        32,3,4,2,0,30,32,3,8,4,0,31,29,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,
        0,33,34,5,19,0,0,34,35,3,6,3,0,35,36,3,8,4,0,36,5,1,0,0,0,37,38,
        7,0,0,0,38,7,1,0,0,0,39,44,3,10,5,0,40,41,7,1,0,0,41,43,3,10,5,0,
        42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,9,1,0,
        0,0,46,44,1,0,0,0,47,52,3,12,6,0,48,49,7,2,0,0,49,51,3,12,6,0,50,
        48,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,11,1,0,0,
        0,54,52,1,0,0,0,55,56,3,14,7,0,56,13,1,0,0,0,57,74,5,16,0,0,58,74,
        5,17,0,0,59,74,5,18,0,0,60,74,5,20,0,0,61,66,5,19,0,0,62,63,5,11,
        0,0,63,64,3,8,4,0,64,65,5,12,0,0,65,67,1,0,0,0,66,62,1,0,0,0,66,
        67,1,0,0,0,67,74,1,0,0,0,68,74,3,16,8,0,69,70,5,13,0,0,70,71,3,8,
        4,0,71,72,5,14,0,0,72,74,1,0,0,0,73,57,1,0,0,0,73,58,1,0,0,0,73,
        59,1,0,0,0,73,60,1,0,0,0,73,61,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,
        0,74,15,1,0,0,0,75,84,5,11,0,0,76,81,3,8,4,0,77,78,5,15,0,0,78,80,
        3,8,4,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,
        82,85,1,0,0,0,83,81,1,0,0,0,84,76,1,0,0,0,84,85,1,0,0,0,85,86,1,
        0,0,0,86,87,5,12,0,0,87,17,1,0,0,0,9,20,24,31,44,52,66,73,81,84
    ]

class Deliverable1Parser ( Parser ):

    grammarFileName = "Deliverable1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'['", "']'", "'('", 
                     "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "FLOAT", "STRING", "NAME", "BOOLEAN", "NEWLINE", 
                      "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_assignment_operations = 3
    RULE_expr = 4
    RULE_term = 5
    RULE_factor = 6
    RULE_value = 7
    RULE_array = 8

    ruleNames =  [ "prog", "statement", "assignment", "assignment_operations", 
                   "expr", "term", "factor", "value", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    NUMBER=16
    FLOAT=17
    STRING=18
    NAME=19
    BOOLEAN=20
    NEWLINE=21
    WS=22
    COMMENT=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Deliverable1Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable1Parser.NEWLINE)
            else:
                return self.getToken(Deliverable1Parser.NEWLINE, i)

        def getRuleIndex(self):
            return Deliverable1Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = Deliverable1Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2041856) != 0):
                self.state = 18
                self.statement()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 19
                    self.match(Deliverable1Parser.NEWLINE)


                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(Deliverable1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(Deliverable1Parser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(Deliverable1Parser.ExprContext,0)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = Deliverable1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(Deliverable1Parser.NAME, 0)

        def assignment_operations(self):
            return self.getTypedRuleContext(Deliverable1Parser.Assignment_operationsContext,0)


        def expr(self):
            return self.getTypedRuleContext(Deliverable1Parser.ExprContext,0)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = Deliverable1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(Deliverable1Parser.NAME)
            self.state = 34
            self.assignment_operations()
            self.state = 35
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_assignment_operations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operations" ):
                listener.enterAssignment_operations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operations" ):
                listener.exitAssignment_operations(self)




    def assignment_operations(self):

        localctx = Deliverable1Parser.Assignment_operationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment_operations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.TermContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.TermContext,i)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = Deliverable1Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.term()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                self.term()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.FactorContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.FactorContext,i)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = Deliverable1Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.factor()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 48
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 49
                self.factor()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(Deliverable1Parser.ValueContext,0)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = Deliverable1Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(Deliverable1Parser.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(Deliverable1Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(Deliverable1Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(Deliverable1Parser.BOOLEAN, 0)

        def NAME(self):
            return self.getToken(Deliverable1Parser.NAME, 0)

        def expr(self):
            return self.getTypedRuleContext(Deliverable1Parser.ExprContext,0)


        def array(self):
            return self.getTypedRuleContext(Deliverable1Parser.ArrayContext,0)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = Deliverable1Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(Deliverable1Parser.NUMBER)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(Deliverable1Parser.FLOAT)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(Deliverable1Parser.STRING)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.match(Deliverable1Parser.BOOLEAN)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.match(Deliverable1Parser.NAME)
                self.state = 66
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 62
                    self.match(Deliverable1Parser.T__10)
                    self.state = 63
                    self.expr()
                    self.state = 64
                    self.match(Deliverable1Parser.T__11)


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.array()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 7)
                self.state = 69
                self.match(Deliverable1Parser.T__12)
                self.state = 70
                self.expr()
                self.state = 71
                self.match(Deliverable1Parser.T__13)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.ExprContext,i)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = Deliverable1Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(Deliverable1Parser.T__10)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2041856) != 0):
                self.state = 76
                self.expr()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 77
                    self.match(Deliverable1Parser.T__14)
                    self.state = 78
                    self.expr()
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 86
            self.match(Deliverable1Parser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





