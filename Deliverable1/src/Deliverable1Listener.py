# Generated from grammar/Deliverable1.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Deliverable1Parser import Deliverable1Parser
else:
    from Deliverable1Parser import Deliverable1Parser

# This class defines a complete listener for a parse tree produced by Deliverable1Parser.
class Deliverable1Listener(ParseTreeListener):

    # Enter a parse tree produced by Deliverable1Parser#prog.
    def enterProg(self, ctx:Deliverable1Parser.ProgContext):
        pass

    # Exit a parse tree produced by Deliverable1Parser#prog.
    def exitProg(self, ctx:Deliverable1Parser.ProgContext):
        pass


    # Enter a parse tree produced by Deliverable1Parser#statement.
    def enterStatement(self, ctx:Deliverable1Parser.StatementContext):
        pass

    # Exit a parse tree produced by Deliverable1Parser#statement.
    def exitStatement(self, ctx:Deliverable1Parser.StatementContext):
        pass


    # Enter a parse tree produced by Deliverable1Parser#assignment.
    def enterAssignment(self, ctx:Deliverable1Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by Deliverable1Parser#assignment.
    def exitAssignment(self, ctx:Deliverable1Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by Deliverable1Parser#assignment_operations.
    def enterAssignment_operations(self, ctx:Deliverable1Parser.Assignment_operationsContext):
        pass

    # Exit a parse tree produced by Deliverable1Parser#assignment_operations.
    def exitAssignment_operations(self, ctx:Deliverable1Parser.Assignment_operationsContext):
        pass


    # Enter a parse tree produced by Deliverable1Parser#expr.
    def enterExpr(self, ctx:Deliverable1Parser.ExprContext):
        pass

    # Exit a parse tree produced by Deliverable1Parser#expr.
    def exitExpr(self, ctx:Deliverable1Parser.ExprContext):
        pass


    # Enter a parse tree produced by Deliverable1Parser#term.
    def enterTerm(self, ctx:Deliverable1Parser.TermContext):
        pass

    # Exit a parse tree produced by Deliverable1Parser#term.
    def exitTerm(self, ctx:Deliverable1Parser.TermContext):
        pass


    # Enter a parse tree produced by Deliverable1Parser#factor.
    def enterFactor(self, ctx:Deliverable1Parser.FactorContext):
        pass

    # Exit a parse tree produced by Deliverable1Parser#factor.
    def exitFactor(self, ctx:Deliverable1Parser.FactorContext):
        pass


    # Enter a parse tree produced by Deliverable1Parser#value.
    def enterValue(self, ctx:Deliverable1Parser.ValueContext):
        pass

    # Exit a parse tree produced by Deliverable1Parser#value.
    def exitValue(self, ctx:Deliverable1Parser.ValueContext):
        pass


    # Enter a parse tree produced by Deliverable1Parser#array.
    def enterArray(self, ctx:Deliverable1Parser.ArrayContext):
        pass

    # Exit a parse tree produced by Deliverable1Parser#array.
    def exitArray(self, ctx:Deliverable1Parser.ArrayContext):
        pass



del Deliverable1Parser