grammar Deliverable2;

prog
    : (statement NEWLINE?)* EOF
    ;

statement
    : assignment
    | expr
    | if_statement
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
    
if_statement
    : 'if' condition_or ':' NEWLINE (statement NEWLINE?)* ('elif' condition_or ':' NEWLINE (statement NEWLINE?)*)* ('else:' NEWLINE (statement NEWLINE?)*)?;

condition_or
    : condition_or 'or' condition_and
    | condition_and;

condition_and
    : condition_and 'and' condition_not
    | condition_not
    ;

condition_not
    : 'not' condition_not
    | general_condition
    ;

general_condition
    : '(' condition_or ')'
    | comparison
    | BOOLEAN
    | NAME
    ;

comparison
    : expr (conditional_operations expr)?
    ;

conditional_operations
    : '<'
    | '<='
    | '>'
    | '>='
    | '=='
    | '!='
    ;

expr
    : term (('+' | '-') term)*
    ;

term
    : factor (('*' | '/' | '%') factor)*
    ;

factor
    : ('+' | '-')? value
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