#!/usr/bin/python3
""" contains the class Student """


class Student:
    """ defines class Student """

    def __init__(self, first_name, last_name, age):
        """ initalizes new Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves dictionary representation of a Student instance """
        return self.__dict__
