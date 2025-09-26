grammar Q4;

start: 'a' A 'a' EOF;

A: 'a' A 'a' | B;
B: 'b'*;