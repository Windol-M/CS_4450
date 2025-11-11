grammar Q2;

start: A;

A: '0' A '0' 
    | B;
B: '1' B '0' 
    | ;