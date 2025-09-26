grammar Q3;

start: A* (A* B A* B A*)* EOF;

A: '0';
B: '1';

