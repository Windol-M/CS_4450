# Generated from ../grammar/Deliverable3.g4 by ANTLR 4.13.2
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
        4,1,42,219,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,3,0,43,8,0,5,0,45,8,0,10,0,12,0,48,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,3,1,56,8,1,1,2,1,2,3,2,60,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,
        1,5,3,5,71,8,5,4,5,73,8,5,11,5,12,5,74,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,5,6,88,8,6,10,6,12,6,91,9,6,1,6,1,6,1,6,3,6,96,
        8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,9,5,9,116,8,9,10,9,12,9,119,9,9,1,10,1,10,1,10,1,10,1,
        10,1,10,5,10,127,8,10,10,10,12,10,130,9,10,1,11,1,11,1,11,3,11,135,
        8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,144,8,12,1,13,1,13,
        1,13,1,13,3,13,150,8,13,1,14,1,14,1,15,1,15,1,15,5,15,157,8,15,10,
        15,12,15,160,9,15,1,16,1,16,1,16,5,16,165,8,16,10,16,12,16,168,9,
        16,1,17,3,17,171,8,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,3,18,184,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,5,18,196,8,18,10,18,12,18,199,9,18,3,18,201,8,18,1,
        18,3,18,204,8,18,1,19,1,19,1,19,1,19,5,19,210,8,19,10,19,12,19,213,
        9,19,3,19,215,8,19,1,19,1,19,1,19,0,2,18,20,20,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,0,4,1,0,11,15,1,0,21,26,1,0,
        16,17,1,0,18,20,230,0,46,1,0,0,0,2,55,1,0,0,0,4,59,1,0,0,0,6,61,
        1,0,0,0,8,65,1,0,0,0,10,67,1,0,0,0,12,78,1,0,0,0,14,97,1,0,0,0,16,
        102,1,0,0,0,18,109,1,0,0,0,20,120,1,0,0,0,22,134,1,0,0,0,24,143,
        1,0,0,0,26,145,1,0,0,0,28,151,1,0,0,0,30,153,1,0,0,0,32,161,1,0,
        0,0,34,170,1,0,0,0,36,203,1,0,0,0,38,205,1,0,0,0,40,42,3,2,1,0,41,
        43,5,37,0,0,42,41,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,40,1,0,
        0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,
        1,0,0,0,49,50,5,0,0,1,50,1,1,0,0,0,51,56,3,4,2,0,52,56,3,12,6,0,
        53,56,3,14,7,0,54,56,3,16,8,0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,
        1,0,0,0,55,54,1,0,0,0,56,3,1,0,0,0,57,60,3,6,3,0,58,60,3,30,15,0,
        59,57,1,0,0,0,59,58,1,0,0,0,60,5,1,0,0,0,61,62,5,36,0,0,62,63,3,
        8,4,0,63,64,3,30,15,0,64,7,1,0,0,0,65,66,7,0,0,0,66,9,1,0,0,0,67,
        72,5,41,0,0,68,70,3,2,1,0,69,71,5,37,0,0,70,69,1,0,0,0,70,71,1,0,
        0,0,71,73,1,0,0,0,72,68,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,75,
        1,0,0,0,75,76,1,0,0,0,76,77,5,42,0,0,77,11,1,0,0,0,78,79,5,1,0,0,
        79,80,3,18,9,0,80,81,5,31,0,0,81,89,3,10,5,0,82,83,5,2,0,0,83,84,
        3,18,9,0,84,85,5,31,0,0,85,86,3,10,5,0,86,88,1,0,0,0,87,82,1,0,0,
        0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,95,1,0,0,0,91,89,
        1,0,0,0,92,93,5,3,0,0,93,94,5,31,0,0,94,96,3,10,5,0,95,92,1,0,0,
        0,95,96,1,0,0,0,96,13,1,0,0,0,97,98,5,4,0,0,98,99,3,18,9,0,99,100,
        5,31,0,0,100,101,3,10,5,0,101,15,1,0,0,0,102,103,5,5,0,0,103,104,
        5,36,0,0,104,105,5,6,0,0,105,106,3,30,15,0,106,107,5,31,0,0,107,
        108,3,10,5,0,108,17,1,0,0,0,109,110,6,9,-1,0,110,111,3,20,10,0,111,
        117,1,0,0,0,112,113,10,2,0,0,113,114,5,9,0,0,114,116,3,20,10,0,115,
        112,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,
        19,1,0,0,0,119,117,1,0,0,0,120,121,6,10,-1,0,121,122,3,22,11,0,122,
        128,1,0,0,0,123,124,10,2,0,0,124,125,5,8,0,0,125,127,3,22,11,0,126,
        123,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,
        21,1,0,0,0,130,128,1,0,0,0,131,132,5,7,0,0,132,135,3,22,11,0,133,
        135,3,24,12,0,134,131,1,0,0,0,134,133,1,0,0,0,135,23,1,0,0,0,136,
        137,5,27,0,0,137,138,3,18,9,0,138,139,5,28,0,0,139,144,1,0,0,0,140,
        144,3,26,13,0,141,144,5,10,0,0,142,144,5,36,0,0,143,136,1,0,0,0,
        143,140,1,0,0,0,143,141,1,0,0,0,143,142,1,0,0,0,144,25,1,0,0,0,145,
        149,3,30,15,0,146,147,3,28,14,0,147,148,3,30,15,0,148,150,1,0,0,
        0,149,146,1,0,0,0,149,150,1,0,0,0,150,27,1,0,0,0,151,152,7,1,0,0,
        152,29,1,0,0,0,153,158,3,32,16,0,154,155,7,2,0,0,155,157,3,32,16,
        0,156,154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,
        0,159,31,1,0,0,0,160,158,1,0,0,0,161,166,3,34,17,0,162,163,7,3,0,
        0,163,165,3,34,17,0,164,162,1,0,0,0,165,168,1,0,0,0,166,164,1,0,
        0,0,166,167,1,0,0,0,167,33,1,0,0,0,168,166,1,0,0,0,169,171,7,2,0,
        0,170,169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,3,36,18,
        0,173,35,1,0,0,0,174,204,5,33,0,0,175,204,5,34,0,0,176,204,5,35,
        0,0,177,204,5,10,0,0,178,183,5,36,0,0,179,180,5,29,0,0,180,181,3,
        30,15,0,181,182,5,30,0,0,182,184,1,0,0,0,183,179,1,0,0,0,183,184,
        1,0,0,0,184,204,1,0,0,0,185,204,3,38,19,0,186,187,5,29,0,0,187,188,
        3,30,15,0,188,189,5,30,0,0,189,204,1,0,0,0,190,191,5,36,0,0,191,
        200,5,27,0,0,192,197,3,30,15,0,193,194,5,32,0,0,194,196,3,30,15,
        0,195,193,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,
        0,198,201,1,0,0,0,199,197,1,0,0,0,200,192,1,0,0,0,200,201,1,0,0,
        0,201,202,1,0,0,0,202,204,5,28,0,0,203,174,1,0,0,0,203,175,1,0,0,
        0,203,176,1,0,0,0,203,177,1,0,0,0,203,178,1,0,0,0,203,185,1,0,0,
        0,203,186,1,0,0,0,203,190,1,0,0,0,204,37,1,0,0,0,205,214,5,29,0,
        0,206,211,3,30,15,0,207,208,5,32,0,0,208,210,3,30,15,0,209,207,1,
        0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,215,1,
        0,0,0,213,211,1,0,0,0,214,206,1,0,0,0,214,215,1,0,0,0,215,216,1,
        0,0,0,216,217,5,30,0,0,217,39,1,0,0,0,22,42,46,55,59,70,74,89,95,
        117,128,134,143,149,158,166,170,183,197,200,203,211,214
    ]

class Deliverable3Parser ( Parser ):

    grammarFileName = "Deliverable3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'elif'", "'else'", "'while'", 
                     "'for'", "'in'", "'not'", "'and'", "'or'", "<INVALID>", 
                     "'='", "'+='", "'-='", "'*='", "'/='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "'('", "')'", "'['", "']'", "':'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "IF", "ELIF", "ELSE", "WHILE", "FOR", 
                      "IN", "NOT", "AND", "OR", "BOOLEAN", "ASSIGN", "PLUSEQ", 
                      "MINUSEQ", "MULEQ", "DIVEQ", "PLUS", "MINUS", "MUL", 
                      "DIV", "MOD", "LT", "LE", "GT", "GE", "EQ", "NEQ", 
                      "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "COLON", 
                      "COMMA", "NUMBER", "FLOAT", "STRING", "NAME", "NEWLINE", 
                      "MULTILINE_COMMENT", "COMMENT", "WS", "INDENT", "DEDENT" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_simple_stmt = 2
    RULE_assignment = 3
    RULE_assignment_operations = 4
    RULE_block_body = 5
    RULE_if_statement = 6
    RULE_while_statement = 7
    RULE_for_statement = 8
    RULE_condition_or = 9
    RULE_condition_and = 10
    RULE_condition_not = 11
    RULE_general_condition = 12
    RULE_comparison = 13
    RULE_conditional_operations = 14
    RULE_expr = 15
    RULE_term = 16
    RULE_factor = 17
    RULE_value = 18
    RULE_array = 19

    ruleNames =  [ "prog", "statement", "simple_stmt", "assignment", "assignment_operations", 
                   "block_body", "if_statement", "while_statement", "for_statement", 
                   "condition_or", "condition_and", "condition_not", "general_condition", 
                   "comparison", "conditional_operations", "expr", "term", 
                   "factor", "value", "array" ]

    EOF = Token.EOF
    IF=1
    ELIF=2
    ELSE=3
    WHILE=4
    FOR=5
    IN=6
    NOT=7
    AND=8
    OR=9
    BOOLEAN=10
    ASSIGN=11
    PLUSEQ=12
    MINUSEQ=13
    MULEQ=14
    DIVEQ=15
    PLUS=16
    MINUS=17
    MUL=18
    DIV=19
    MOD=20
    LT=21
    LE=22
    GT=23
    GE=24
    EQ=25
    NEQ=26
    LPAREN=27
    RPAREN=28
    LBRACKET=29
    RBRACKET=30
    COLON=31
    COMMA=32
    NUMBER=33
    FLOAT=34
    STRING=35
    NAME=36
    NEWLINE=37
    MULTILINE_COMMENT=38
    COMMENT=39
    WS=40
    INDENT=41
    DEDENT=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Deliverable3Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable3Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Deliverable3Parser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.NEWLINE)
            else:
                return self.getToken(Deliverable3Parser.NEWLINE, i)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = Deliverable3Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 129386087474) != 0):
                self.state = 40
                self.statement()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 41
                    self.match(Deliverable3Parser.NEWLINE)


                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(Deliverable3Parser.EOF)
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

        def simple_stmt(self):
            return self.getTypedRuleContext(Deliverable3Parser.Simple_stmtContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(Deliverable3Parser.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(Deliverable3Parser.While_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(Deliverable3Parser.For_statementContext,0)


        def getRuleIndex(self):
            return Deliverable3Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = Deliverable3Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 16, 17, 29, 33, 34, 35, 36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.simple_stmt()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.if_statement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.while_statement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.for_statement()
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


    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(Deliverable3Parser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(Deliverable3Parser.ExprContext,0)


        def getRuleIndex(self):
            return Deliverable3Parser.RULE_simple_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_stmt" ):
                listener.enterSimple_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_stmt" ):
                listener.exitSimple_stmt(self)




    def simple_stmt(self):

        localctx = Deliverable3Parser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple_stmt)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
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
            return self.getToken(Deliverable3Parser.NAME, 0)

        def assignment_operations(self):
            return self.getTypedRuleContext(Deliverable3Parser.Assignment_operationsContext,0)


        def expr(self):
            return self.getTypedRuleContext(Deliverable3Parser.ExprContext,0)


        def getRuleIndex(self):
            return Deliverable3Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = Deliverable3Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(Deliverable3Parser.NAME)
            self.state = 62
            self.assignment_operations()
            self.state = 63
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

        def ASSIGN(self):
            return self.getToken(Deliverable3Parser.ASSIGN, 0)

        def PLUSEQ(self):
            return self.getToken(Deliverable3Parser.PLUSEQ, 0)

        def MINUSEQ(self):
            return self.getToken(Deliverable3Parser.MINUSEQ, 0)

        def MULEQ(self):
            return self.getToken(Deliverable3Parser.MULEQ, 0)

        def DIVEQ(self):
            return self.getToken(Deliverable3Parser.DIVEQ, 0)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_assignment_operations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operations" ):
                listener.enterAssignment_operations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operations" ):
                listener.exitAssignment_operations(self)




    def assignment_operations(self):

        localctx = Deliverable3Parser.Assignment_operationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment_operations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0)):
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


    class Block_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(Deliverable3Parser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(Deliverable3Parser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable3Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Deliverable3Parser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.NEWLINE)
            else:
                return self.getToken(Deliverable3Parser.NEWLINE, i)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_block_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_body" ):
                listener.enterBlock_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_body" ):
                listener.exitBlock_body(self)




    def block_body(self):

        localctx = Deliverable3Parser.Block_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(Deliverable3Parser.INDENT)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.statement()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 69
                    self.match(Deliverable3Parser.NEWLINE)


                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 129386087474) != 0)):
                    break

            self.state = 76
            self.match(Deliverable3Parser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Deliverable3Parser.IF, 0)

        def condition_or(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable3Parser.Condition_orContext)
            else:
                return self.getTypedRuleContext(Deliverable3Parser.Condition_orContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.COLON)
            else:
                return self.getToken(Deliverable3Parser.COLON, i)

        def block_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable3Parser.Block_bodyContext)
            else:
                return self.getTypedRuleContext(Deliverable3Parser.Block_bodyContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.ELIF)
            else:
                return self.getToken(Deliverable3Parser.ELIF, i)

        def ELSE(self):
            return self.getToken(Deliverable3Parser.ELSE, 0)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = Deliverable3Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(Deliverable3Parser.IF)
            self.state = 79
            self.condition_or(0)
            self.state = 80
            self.match(Deliverable3Parser.COLON)
            self.state = 81
            self.block_body()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 82
                self.match(Deliverable3Parser.ELIF)
                self.state = 83
                self.condition_or(0)
                self.state = 84
                self.match(Deliverable3Parser.COLON)
                self.state = 85
                self.block_body()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 92
                self.match(Deliverable3Parser.ELSE)
                self.state = 93
                self.match(Deliverable3Parser.COLON)
                self.state = 94
                self.block_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(Deliverable3Parser.WHILE, 0)

        def condition_or(self):
            return self.getTypedRuleContext(Deliverable3Parser.Condition_orContext,0)


        def COLON(self):
            return self.getToken(Deliverable3Parser.COLON, 0)

        def block_body(self):
            return self.getTypedRuleContext(Deliverable3Parser.Block_bodyContext,0)


        def getRuleIndex(self):
            return Deliverable3Parser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = Deliverable3Parser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(Deliverable3Parser.WHILE)
            self.state = 98
            self.condition_or(0)
            self.state = 99
            self.match(Deliverable3Parser.COLON)
            self.state = 100
            self.block_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Deliverable3Parser.FOR, 0)

        def NAME(self):
            return self.getToken(Deliverable3Parser.NAME, 0)

        def IN(self):
            return self.getToken(Deliverable3Parser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(Deliverable3Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(Deliverable3Parser.COLON, 0)

        def block_body(self):
            return self.getTypedRuleContext(Deliverable3Parser.Block_bodyContext,0)


        def getRuleIndex(self):
            return Deliverable3Parser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)




    def for_statement(self):

        localctx = Deliverable3Parser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(Deliverable3Parser.FOR)
            self.state = 103
            self.match(Deliverable3Parser.NAME)
            self.state = 104
            self.match(Deliverable3Parser.IN)
            self.state = 105
            self.expr()
            self.state = 106
            self.match(Deliverable3Parser.COLON)
            self.state = 107
            self.block_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_and(self):
            return self.getTypedRuleContext(Deliverable3Parser.Condition_andContext,0)


        def condition_or(self):
            return self.getTypedRuleContext(Deliverable3Parser.Condition_orContext,0)


        def OR(self):
            return self.getToken(Deliverable3Parser.OR, 0)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_condition_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_or" ):
                listener.enterCondition_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_or" ):
                listener.exitCondition_or(self)



    def condition_or(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Deliverable3Parser.Condition_orContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_condition_or, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.condition_and(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Deliverable3Parser.Condition_orContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition_or)
                    self.state = 112
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 113
                    self.match(Deliverable3Parser.OR)
                    self.state = 114
                    self.condition_and(0) 
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Condition_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_not(self):
            return self.getTypedRuleContext(Deliverable3Parser.Condition_notContext,0)


        def condition_and(self):
            return self.getTypedRuleContext(Deliverable3Parser.Condition_andContext,0)


        def AND(self):
            return self.getToken(Deliverable3Parser.AND, 0)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_condition_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_and" ):
                listener.enterCondition_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_and" ):
                listener.exitCondition_and(self)



    def condition_and(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Deliverable3Parser.Condition_andContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_condition_and, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.condition_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Deliverable3Parser.Condition_andContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition_and)
                    self.state = 123
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 124
                    self.match(Deliverable3Parser.AND)
                    self.state = 125
                    self.condition_not() 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Condition_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(Deliverable3Parser.NOT, 0)

        def condition_not(self):
            return self.getTypedRuleContext(Deliverable3Parser.Condition_notContext,0)


        def general_condition(self):
            return self.getTypedRuleContext(Deliverable3Parser.General_conditionContext,0)


        def getRuleIndex(self):
            return Deliverable3Parser.RULE_condition_not

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_not" ):
                listener.enterCondition_not(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_not" ):
                listener.exitCondition_not(self)




    def condition_not(self):

        localctx = Deliverable3Parser.Condition_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_condition_not)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(Deliverable3Parser.NOT)
                self.state = 132
                self.condition_not()
                pass
            elif token in [10, 16, 17, 27, 29, 33, 34, 35, 36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.general_condition()
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


    class General_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Deliverable3Parser.LPAREN, 0)

        def condition_or(self):
            return self.getTypedRuleContext(Deliverable3Parser.Condition_orContext,0)


        def RPAREN(self):
            return self.getToken(Deliverable3Parser.RPAREN, 0)

        def comparison(self):
            return self.getTypedRuleContext(Deliverable3Parser.ComparisonContext,0)


        def BOOLEAN(self):
            return self.getToken(Deliverable3Parser.BOOLEAN, 0)

        def NAME(self):
            return self.getToken(Deliverable3Parser.NAME, 0)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_general_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneral_condition" ):
                listener.enterGeneral_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneral_condition" ):
                listener.exitGeneral_condition(self)




    def general_condition(self):

        localctx = Deliverable3Parser.General_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_general_condition)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(Deliverable3Parser.LPAREN)
                self.state = 137
                self.condition_or(0)
                self.state = 138
                self.match(Deliverable3Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.comparison()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.match(Deliverable3Parser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.match(Deliverable3Parser.NAME)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Deliverable3Parser.ExprContext,i)


        def conditional_operations(self):
            return self.getTypedRuleContext(Deliverable3Parser.Conditional_operationsContext,0)


        def getRuleIndex(self):
            return Deliverable3Parser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = Deliverable3Parser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.expr()
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 146
                self.conditional_operations()
                self.state = 147
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_operationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(Deliverable3Parser.LT, 0)

        def LE(self):
            return self.getToken(Deliverable3Parser.LE, 0)

        def GT(self):
            return self.getToken(Deliverable3Parser.GT, 0)

        def GE(self):
            return self.getToken(Deliverable3Parser.GE, 0)

        def EQ(self):
            return self.getToken(Deliverable3Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(Deliverable3Parser.NEQ, 0)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_conditional_operations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_operations" ):
                listener.enterConditional_operations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_operations" ):
                listener.exitConditional_operations(self)




    def conditional_operations(self):

        localctx = Deliverable3Parser.Conditional_operationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_conditional_operations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0)):
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
                return self.getTypedRuleContexts(Deliverable3Parser.TermContext)
            else:
                return self.getTypedRuleContext(Deliverable3Parser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.PLUS)
            else:
                return self.getToken(Deliverable3Parser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.MINUS)
            else:
                return self.getToken(Deliverable3Parser.MINUS, i)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = Deliverable3Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.term()
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 154
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==17):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 155
                    self.term() 
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
                return self.getTypedRuleContexts(Deliverable3Parser.FactorContext)
            else:
                return self.getTypedRuleContext(Deliverable3Parser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.MUL)
            else:
                return self.getToken(Deliverable3Parser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.DIV)
            else:
                return self.getToken(Deliverable3Parser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.MOD)
            else:
                return self.getToken(Deliverable3Parser.MOD, i)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = Deliverable3Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.factor()
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 162
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 163
                    self.factor() 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
            return self.getTypedRuleContext(Deliverable3Parser.ValueContext,0)


        def PLUS(self):
            return self.getToken(Deliverable3Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(Deliverable3Parser.MINUS, 0)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = Deliverable3Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16 or _la==17:
                self.state = 169
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 172
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
            return self.getToken(Deliverable3Parser.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(Deliverable3Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(Deliverable3Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(Deliverable3Parser.BOOLEAN, 0)

        def NAME(self):
            return self.getToken(Deliverable3Parser.NAME, 0)

        def LBRACKET(self):
            return self.getToken(Deliverable3Parser.LBRACKET, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Deliverable3Parser.ExprContext,i)


        def RBRACKET(self):
            return self.getToken(Deliverable3Parser.RBRACKET, 0)

        def array(self):
            return self.getTypedRuleContext(Deliverable3Parser.ArrayContext,0)


        def LPAREN(self):
            return self.getToken(Deliverable3Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Deliverable3Parser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.COMMA)
            else:
                return self.getToken(Deliverable3Parser.COMMA, i)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = Deliverable3Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(Deliverable3Parser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(Deliverable3Parser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(Deliverable3Parser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.match(Deliverable3Parser.BOOLEAN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.match(Deliverable3Parser.NAME)
                self.state = 183
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 179
                    self.match(Deliverable3Parser.LBRACKET)
                    self.state = 180
                    self.expr()
                    self.state = 181
                    self.match(Deliverable3Parser.RBRACKET)


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 185
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 186
                self.match(Deliverable3Parser.LBRACKET)
                self.state = 187
                self.expr()
                self.state = 188
                self.match(Deliverable3Parser.RBRACKET)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 190
                self.match(Deliverable3Parser.NAME)
                self.state = 191
                self.match(Deliverable3Parser.LPAREN)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 129386087424) != 0):
                    self.state = 192
                    self.expr()
                    self.state = 197
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==32:
                        self.state = 193
                        self.match(Deliverable3Parser.COMMA)
                        self.state = 194
                        self.expr()
                        self.state = 199
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 202
                self.match(Deliverable3Parser.RPAREN)
                pass


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

        def LBRACKET(self):
            return self.getToken(Deliverable3Parser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(Deliverable3Parser.RBRACKET, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Deliverable3Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable3Parser.COMMA)
            else:
                return self.getToken(Deliverable3Parser.COMMA, i)

        def getRuleIndex(self):
            return Deliverable3Parser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = Deliverable3Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(Deliverable3Parser.LBRACKET)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 129386087424) != 0):
                self.state = 206
                self.expr()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==32:
                    self.state = 207
                    self.match(Deliverable3Parser.COMMA)
                    self.state = 208
                    self.expr()
                    self.state = 213
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 216
            self.match(Deliverable3Parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.condition_or_sempred
        self._predicates[10] = self.condition_and_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_or_sempred(self, localctx:Condition_orContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def condition_and_sempred(self, localctx:Condition_andContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




