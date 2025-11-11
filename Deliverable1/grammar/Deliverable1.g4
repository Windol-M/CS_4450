grammar Deliverable1;

prog
    : (statement NEWLINE?)* EOF
    ;

statement
    : assignment
    | expr
    ;

assignment
    : NAME assignment_operations expr
    ;

assignment_operations
    : '=' 
    | '+=' 
    | '-=' 
    | '*=' 
    | '/='
    ;

expr
    : term (('+' | '-') term)*
    ;

term
    : factor (('*' | '/' | '%') factor)*
    ;

factor
    : value
    ;

value
    : NUMBER
    | FLOAT
    | STRING
    | BOOLEAN
    | NAME ('[' expr ']')?
    | array
    | '(' expr ')'
    ;

NUMBER  : [0-9]+ ;

FLOAT   : [0-9]+ '.' [0-9]+ ;

STRING : '"' .*? '"' | '\'' .*? '\'';

NAME : [a-zA-Z_][a-zA-Z_0-9]*;

array
    : '[' (expr (',' expr)*)? ']'
    ;

BOOLEAN : 'True' | 'False';

NEWLINE : ('\r'? '\n')+;
WS : [ \t]+ -> skip;
COMMENT : '#' .*? ('\n' | EOF) -> skip;

