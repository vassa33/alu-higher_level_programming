#!/usr/bin/python3
""" contains the class Student """


class Student:
    """ defines class Student """

    def __init__(self, first_name, last_name, age):
        """ initalizes new Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dictionary representation of a Student instance """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for att in attrs:
            if type(att) is not str:
                return self.__dict__
        return {x: self.__dict__[x] for x in self.__dict__ if x in attrs}

    def reload_from_json(self, json):
        """ replaces all attributes of Student instance """
        for key, value in json.items():
            self.__dict__[key] = value
