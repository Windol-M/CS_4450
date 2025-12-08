grammar Deliverable3;

tokens { INDENT, DEDENT }

@lexer::header {
import collections
from antlr4.Token import CommonToken, Token
from Deliverable3Parser import Deliverable3Parser 
}

@lexer::members { 
indents = [0]
tokens = collections.deque()
at_start_of_line = True

def nextToken(self):
    if self.tokens:
        return self.tokens.popleft()
    
    t = super().nextToken()

    # Handle dedents at start of line when there's no leading whitespace
    if self.at_start_of_line and t.type not in [self.WS, self.NEWLINE, Token.EOF]:
        self.at_start_of_line = False
        indent = 0
        
        # Generate DEDENTs if we've decreased indentation
        while len(self.indents) > 1 and self.indents[-1] > indent:
            self.indents.pop()
            self.tokens.append(self.create_token(Deliverable3Parser.DEDENT, ''))
        
        if self.tokens:
            self.tokens.append(t)
            return self.tokens.popleft()

    if t.type == Token.EOF and len(self.indents) > 1:
        while len(self.indents) > 1:
            self.indents.pop()
            self.tokens.append(self.create_token(Deliverable3Parser.DEDENT, ''))
        
        self.tokens.append(t)
        return self.tokens.popleft()

    return t

def create_token(self, token_type, text):
    from antlr4.Token import CommonToken
    token = CommonToken(type=token_type)
    token.text = text
    token.channel = self._channel
    return token
}

prog
    : (statement NEWLINE?)* EOF
    ;

statement
    : assignment
    | expr
    | if_statement
    | while_statement
    | for_statement
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
    : 'if' condition_or ':' NEWLINE INDENT (statement NEWLINE?)* DEDENT ('elif' condition_or ':' NEWLINE INDENT (statement NEWLINE?)* DEDENT)* ('else:' NEWLINE INDENT (statement NEWLINE?)* DEDENT)?;

while_statement
    : 'while' condition_or ':' NEWLINE INDENT (statement NEWLINE?)* DEDENT
    ;

for_statement
    : 'for' NAME 'in' expr ':' NEWLINE INDENT (statement NEWLINE?)* DEDENT
    ;

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
    | '[' expr ']'
    | NAME '(' (expr (',' expr)*)? ')'
    ;

LPAREN  : '(';
RPAREN  : ')';

MULTILINE_COMMENT
    : ( '\'\'\'' .*? '\'\'\'' 
      | '"""' .*? '"""'
      ) -> skip
    ;

NUMBER  : [0-9]+ ;

FLOAT   : [0-9]+ '.' [0-9]+ ;

STRING : '"' .*? '"' | '\'' .*? '\'';

NAME : [a-zA-Z_][a-zA-Z_0-9]*;

array
    : '[' (expr (',' expr)*)? ']'
    ;

BOOLEAN : 'True' | 'False';

NEWLINE : ('\r'? '\n')+
    {self.at_start_of_line = True}
;
WS : [ \t]+ {
if self.at_start_of_line:
    self.at_start_of_line = False

    indent = len(self.text.replace('\t', '        '))
    current_indent = self.indents[-1]

    if indent > current_indent:
        self.indents.append(indent)
        self.tokens.append(self.create_token(Deliverable3Parser.INDENT, self.text))
    elif indent < current_indent:
        while len(self.indents) > 1 and self.indents[-1] > indent:
            self.indents.pop()
            self.tokens.append(self.create_token(Deliverable3Parser.DEDENT, ''))
        if self.indents[-1] != indent:
            print(f"Error: Indent level {indent} does not match any previous level {self.indents}")

    self.skip()
else:
    self.skip()
};

COMMENT : '#' .*? ('\n' | EOF) -> skip;
