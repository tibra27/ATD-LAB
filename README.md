# ATD-LAB
Assignments related to Advance topics in Databases
----------------------------------------------------------------------------------------------------------------------------------------

ASSIGNMENT-1
------------
Design as well as implement a parser for the subset of SQL with the following constructs:
1) CREATE TABLE statement
2) DROP TABLE statement
3) SELECT statement
4) INSERT statement
5) UPDATE statement
6) DELETE statement

For this task follow two steps:
1) Write context free grammar(CFG) for above SQL statements.
2) Make the parser using the grammar.

INPUT-SQL query

OUTPUT-Parse tree for given SQL statement and error if syntactically wrong.

Reference:
http://www.dabeaz.com/ply/ply.html


----------------------------------------------------------------------------------------------------------------------------------------
ASSIGNMENT-2
------------
Implement an Equivalent Relational algebric expression generator which gives all the equivalent expressions using Equivalence Rules of relational algebra.

INPUT- Single relational algebric expression

OUTPUT- All expression that are euivalent to given expression.

NOTE: All the instructions related to I/O format are specified in the Script itself.


----------------------------------------------------------------------------------------------------------------------------------------
ASSIGNMENT-3
------------
Write a Program which shall read a concurrent schedule involving n transactions with read and write instructions on data items from an input file (sample input file attached) and find whether the schedule is Conflict Serializable or not using the graph-based method discussed in the class. 

In case of conflict serializable schedule, your program shall also give the serializability order as well and for non-serializable schedule, give the cycle(s) present in the graph.

The sample input contains 3 transactions (T1, T2, T3) and 3 data items (A, B, C) however your program shall be able to handle any finite number of transactions and data items. There shall not be any constraints on number of transactions and data items.



