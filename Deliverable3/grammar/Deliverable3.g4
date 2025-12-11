grammar Deliverable3;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from Deliverable3Parser import Deliverable3Parser
}
@lexer::members {
class Deliverable3Denter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: Deliverable3Lexer = lexer

    def pull_token(self):
        return super(Deliverable3Lexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.Deliverable3Denter(self, self.NEWLINE, Deliverable3Parser.INDENT, Deliverable3Parser.DEDENT, False)
    return self.denter.next_token()

}

prog
    : (statement NEWLINE?)* EOF
    ;

statement
    : simple_stmt
    | if_statement
    | while_statement
    | for_statement
    ;

simple_stmt
    : assignment
    | expr
    ;

assignment
    : NAME assignment_operations expr
    ;

assignment_operations
    : ASSIGN
    | PLUSEQ
    | MINUSEQ
    | MULEQ
    | DIVEQ
    ;

block_body
    : INDENT (statement NEWLINE?)+ DEDENT
    ;

if_statement
    : IF condition_or COLON
      block_body
      (ELIF condition_or COLON block_body)*
      (ELSE COLON block_body)?
    ;

while_statement
    : WHILE condition_or COLON
      block_body
    ;

for_statement
    : FOR NAME IN expr COLON
      block_body
    ;

condition_or
    : condition_or OR condition_and
    | condition_and
    ;

condition_and
    : condition_and AND condition_not
    | condition_not
    ;

condition_not
    : NOT condition_not
    | general_condition
    ;

general_condition
    : LPAREN condition_or RPAREN
    | comparison
    | BOOLEAN
    | NAME
    ;

comparison
    : expr (conditional_operations expr)?
    ;

conditional_operations
    : LT
    | LE
    | GT
    | GE
    | EQ
    | NEQ
    ;

expr
    : term ((PLUS | MINUS) term)*
    ;

term
    : factor ((MUL | DIV | MOD) factor)*
    ;

factor
    : (PLUS | MINUS)? value
    ;

value
    : NUMBER
    | FLOAT
    | STRING
    | BOOLEAN
    | NAME (LBRACKET expr RBRACKET)?
    | array
    | LBRACKET expr RBRACKET
    | NAME LPAREN (expr (COMMA expr)*)? RPAREN
    ;

array
    : LBRACKET (expr (COMMA expr)*)? RBRACKET
    ;

IF      : 'if';
ELIF    : 'elif';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';
IN      : 'in';
NOT     : 'not';
AND     : 'and';
OR      : 'or';

BOOLEAN : 'True' | 'False';

ASSIGN  : '=';
PLUSEQ  : '+=';
MINUSEQ : '-=';
MULEQ   : '*=';
DIVEQ   : '/=';

PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';
MOD     : '%';

LT      : '<';
LE      : '<=';
GT      : '>';
GE      : '>=';
EQ      : '==';
NEQ     : '!=';

LPAREN  : '(';
RPAREN  : ')';
LBRACKET  : '[';
RBRACKET  : ']';
COLON   : ':';
COMMA   : ',';

NUMBER  : [0-9]+ ;
FLOAT   : [0-9]+ '.' [0-9]+ ;

STRING
    : '"'  ( ~["\\] | '\\' . )* '"'
    | '\'' ( ~['\\] | '\\' . )* '\''
    ;

NAME : [a-zA-Z_][a-zA-Z_0-9]*;

NEWLINE : ('\r'? '\n' '\t'*);

MULTILINE_COMMENT
    : ( '\'\'\'' .*? '\'\'\''
      | '"""'  .*? '"""'
      ) -> skip
    ;

COMMENT
    : '#' .*? ('\n' | EOF) -> skip
    ;

WS : [ \t]+ -> skip;