#!/usr/bin/python3
""" Creates class MyList """


class MyList(list):
    """ defines MyList class """
    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
