grammar Deliverable3;

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

if_statement
    : IF condition_or COLON NEWLINE
      (statement NEWLINE?)*
      (ELIF condition_or COLON NEWLINE (statement NEWLINE?)*)*
      (ELSE COLON NEWLINE (statement NEWLINE?)*)?
    ;

while_statement
    : WHILE condition_or COLON NEWLINE
      (statement NEWLINE?)*
    ;

for_statement
    : FOR NAME IN expr COLON NEWLINE
      (statement NEWLINE?)*
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

NEWLINE : ('\r'? '\n')+ ;

MULTILINE_COMMENT
    : ( '\'\'\'' .*? '\'\'\''
      | '"""'  .*? '"""'
      ) -> skip
    ;

COMMENT
    : '#' .*? ('\n' | EOF) -> skip
    ;

WS : [ \t]+ -> skip;
