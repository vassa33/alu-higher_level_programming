# PYTHON - Classes and Objects

## General - Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

> Why Python programming is awesome.  
> What is OOP.  
> “first-class everything”.  
> What is a class.  
> What is an object and an instance.  
> What is the difference between a class and an object or instance.  
> What is an attribute.  
> What are and how to use public, protected and private attributes.  
> What is self.  
> What is a method.  
> What is the special __init__ method and how to use it.  
> What is Data Abstraction, Data Encapsulation, and Information Hiding.  
> What is a property.  
> What is the difference between an attribute and a property in Python.  
> What is the Pythonic way to write getters and setters in Python.  
> How to dynamically create arbitrary new attributes for existing instances of a class.  
> How to bind attributes to object and classes.  
> What is the __dict__ of a class and/or instance of a class and what does it contain.  
> How does Python find the attributes of an object or class.  
> How to use the getattr function.  

## Resources:-
> Object Oriented Programming - https://python.swaroopch.com/oop.html  (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)  
> Object-Oriented Programming - https://python-course.eu/oop/object-oriented-programming.php  
> Properties vs. Getters and Setters - https://python-course.eu/oop/properties-vs-getters-and-setters.php  
> Learn to Program 9 : Object Oriented Programming - https://www.youtube.com/watch?v=1AGyBuVCTeE  
> Python Classes and Objects (Socratica) - https://www.youtube.com/watch?v=apACNr7DC_s
> Object Oriented Programming (MIT OpenCourseWare) - https://www.youtube.com/watch?v=-DP1i2ZU9gk  

## N/B:- 
>> All your modules should have a documentation 
>> All your classes should have a documentation 
>> All your functions (inside and outside a class) should have a documentation
>> A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# Tasks:- 

## 0. My first square

Write an empty class Square that defines a square:

You are not allowed to import any module

## 1. Square with size

Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module

## 2. Size validation

Write a class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
You are not allowed to import any module

## 3. Area of a square

Write a class Square that defines a square by: (based on 2-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Public instance method: def area(self): that returns the current square area
You are not allowed to import any module

## 4. Access and update private attribute

Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception with the message size     must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >=     0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
You are not allowed to import any module

## 5. Printing a square

Write a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception with the message size    must be an integer
   if size is less than 0, raise a ValueError exception with the message size must be >=    0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
You are not allowed to import any module 

## 6. Coordinates of a square
mandatory
Write a class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
        size must be an integer, otherwise raise a TypeError exception with the message           size must be an integer
        if size is less than 0, raise a ValueError exception with the message size must           be >=  0
Private instance attribute: position:
    property def position(self): to retrieve it
    property setter def position(self, value): to set it:
          position must be a tuple of 2 positive integers, otherwise raise a TypeError             exception with the message position must be a tuple of 2 positive integers
Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
      if size is equal to 0, print an empty line
      position should be use by using space - Don’t fill lines by spaces when position[1]       > 0
You are not allowed to import any module
