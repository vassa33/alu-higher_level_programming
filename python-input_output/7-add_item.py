#!/usr/bin/python3
""" contains the add_item function """
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    """testing for error"""
    my_list = load_from_json_file(filename)
except:
    """handling any error encountered"""
    my_list = []
for arg in argv[1:]:
    """appending arguments to the list,
    and saving it to a JSON file"""
    my_list.append(arg)
save_to_json_file(my_list, filename)
