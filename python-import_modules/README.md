# PYTHON - import & modules

## General - Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
>Why Python programming is awesome
>How to import functions from another file
>How to use imported functions
>How to create a module
>How to use the built-in function dir()
>How to prevent code in your script from being executed when imported
>How to use command line arguments with your Python programs

# Tasks:-

## 0. Import a simple function from a simple file
mandatory
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

You have to use print function with string format to display integers
You have to assign:
the value 1 to a variable called a
the value 2 to a variable called b
and use those two variables as arguments when calling the functions add and print
a and b must be defined in 2 different lines: a = 1 and another b = 2
Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
You can only use the word add_0 once in your code
You are not allowed to use * for importing or __import__
Your code should not be executed when imported - by using __import__, like the example below
