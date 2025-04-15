from lib.most_often import *

"""
Given a an empty list, starting_list returns the empty list
"""

def test_starting_list_returns_an_empty_list():
    test_instance = MostOften([])
    result = test_instance.starting_list
    assert result == []

"""
Given a list, starting_list returns the list
"""

def test_starting_list_returns_a_given_starting_list():
    test_instance = MostOften(["rick", "jude", "cammie"])
    result = test_instance.starting_list
    assert result == ["rick", "jude", "cammie"]


#!!! WIP: 

# """
# Given a new item "flick", add_new will return the 
# original list with "flick" added to it
# """

# def test_add_new_will_add_new_item_to_list():
#     test_instance = MostOften(["rick", "jude", "cammie"])
#     result = test_instance.new_item("flick")
#     assert result == ["rick", "jude", "cammie", "flick"]


    #!!! Leaving unfinished