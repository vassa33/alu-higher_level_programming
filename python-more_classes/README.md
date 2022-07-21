# PYTHON - More Classes and Objects

## General - Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:


> Why Python programming is awesome  
> What is OOP   
> “first-class everything”  
> What is a class  
> What is an object and an instance  
> What is the difference between a class and an object or instance  
> What is an attribute  
> What are and how to use public, protected and private attributes  
> What is self  
> What is a method  
> What is the special __init__ method and how to use it  
> What is Data Abstraction, Data Encapsulation, and Information Hiding  
> What is a property  
> What is the difference between an attribute and a property in Python    
> What is the Pythonic way to write getters and setters in Python  
> What are the special __str__ and __repr__ methods and how to use them  
> What is the difference between __str__ and __repr__  
> What is a class attribute  
> What is the difference between a object attribute and a class attribute  
> What is a class method  
> What is a static method  
> How to dynamically create arbitrary new attributes for existing instances of a class  
> How to bind attributes to object and classes  
> What is and what does contain __dict__ of a class and of an instance of a class  
> How does Python find the attributes of an object or class  
> How to use the getattr function  

# Tasks:-  

## 0-rectangle.py  

create class Rectangle that defines a rectangle

## 1-rectangle.py 

Empty class Rectangle with:

private instance attribute width  
property def width(self): to retrieve it  
property setter def width(self, value): to set it  
private instance attribute height  
property ef height(self): to retrieve it  
property setter def height(self, value): to set it  
instantiation with optional width and height: def __init__(self, width=0, height=0):  

## 2-rectangle.py 

class Rectangle with all of the above and:  

public instance method def area(self): that returns the rectangle's area  
public instance method def perimeter(self): that returns the rectangle's perimeter  

## 3-rectangle.py 

class Rectangle with all of the above and:  

print() and str() should print the rectangle with the character #  

## 4-rectangle.py 

class Rectangle with all of the above and:

repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()  

## 5-rectangle.py 

class Rectangle with all of the above and:

prints the message Bye rectangle... when an instance of Rectangle is deleted  

## 6-rectangle.py 

class Rectangle with all of the above and:

public class attribute number_of_instances:  
initialized to 0  
incremented during new instance initialization  
decremented during instance deletion  

## 7-rectangle.py 

class Rectangle with all of the above and:

public class attribute print_symbol:    
initialized as #  
can be any symbol and any type  
8-rectangle.py - class Rectangle with all of the above and:  

static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on area  

## 9-rectangle.py 

class Rectangle with all of the above and:

class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size  
