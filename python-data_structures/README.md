# PYTHON - Data Structures: Lists, Tuples

## General - Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
>Why Python programming is awesome
>What are lists and how to use them
>What are the differences and similarities between strings and lists
>What are the most common methods of lists and how to use them
>How to use lists as stacks and queues
>What are list comprehensions and how to use them
>What are tuples and how to use them
>When to use tuples versus lists
>What is a sequence
>What is tuple packing
>What is seqence unpacking
>What is the del statement and how to use it

## Supporting Material:-
Data structures (until 5.3. Tuples and Sequences included) - https://docs.python.org/3/tutorial/datastructures.html 
3.1.3 Lists - https://docs.python.org/3/tutorial/introduction.html#lists
Learn to Program 6: Lists (YouTube) - https://www.youtube.com/watch?v=A1HUzrvS-Pw 

# Tasks :-
## 0. Print a list of integers

Write a function that prints all integers of a list.

Prototype: def print_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers

## 1. Secure access to an element in a list

Write a function that retrieves an element from a list like in C.

Prototype: def element_at(my_list, idx):
If idx is negative, the function should return None
If idx is out of range (> of number of element in my_list), the function should return None
You are not allowed to import any module
You are not allowed to use try/except 
