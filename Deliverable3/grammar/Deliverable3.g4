grammar Deliverable3;

tokens { INDENT, DEDENT }

@lexer::members {
    import collections

    indents = [0]

    tokens = collections.deque()

    at_start_of_line = True

    def next_token(self):
        if self.tokens:
            return self.tokens.popleft()
        
        t = super().next_token()

        if t.type == Eof and len(self.indents) > 1:
            while len(self.indents) > 1:
                self.indents.pop()
                self.tokens.append(self.create_token(DEDENT, ''))
            
            self.tokens.append(t)
            return self.tokens.popleft()

        return t

    def create_token(self, token_type, text):
        return CommonToken(self._tokenFactorySourcePair, token_type, self.channel, self.tokenStartCharIndex, self._input.index() - 1, text)
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
    : 'if' condition_or ':' NEWLINE (statement NEWLINE?)* ('elif' condition_or ':' NEWLINE (statement NEWLINE?)*)* ('else:' NEWLINE (statement NEWLINE?)*)?;

while_statement
    : 'while' condition_or ':' NEWLINE (statement NEWLINE?)*
    ;

for_statement
    : 'for' NAME 'in' expr ':' NEWLINE (statement NEWLINE?)*
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
WS : [ \t]+ 
    {
        if self.at_start_of_line:
            self.at_start_of_line = False
            
            indent = self.text.replace('\t', '        ').count(' ')
            current_indent = self.indents[-1]

            if indent > current_indent:
                self.indents.append(indent)
                self.tokens.append(self.createToken(INDENT, self.text))
            
            elif indent < current_indent:
                while len(self.indents) > 1 and self.indents[-1] > indent:
                    self.indents.pop()
                    self.tokens.append(self.createToken(DEDENT, ''))

                if indent != self.indents[-1]:
                    print(f"Error: Indent level {indent} does not match any previous level.")
                    
            self.skip()
        else:
            self.skip()
    }
;

COMMENT : '#' .*? ('\n' | EOF) -> skip;
