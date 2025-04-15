from lib.todo_tracker import *


"""
No tasks to start with
"""
def test_class_returns_no_tasks_with_no_tasks_added():
    test_instance = TodoList()
    test_instance.view_items() # returns []
    assert test_instance.view_items() == []

"""
When a item is added
the item is added to items_list
"""
def test_class_returns_list_with_item_added_to_it():
    test_instance = TodoList()
    test_instance.add("Wash dog")
    assert test_instance.view_items() == ["Wash dog"] # returns ["wash dog"]


"""
When multiple item are added
the items are added to items_list
"""
def test_class_returns_item_list_with_multiple_items_added():
    test_instance = TodoList()
    test_instance.add("Wash dog")
    test_instance.add("Feed cat")
    test_instance.add("Brush hair")
    assert test_instance.view_items() == ["Wash dog", "Feed cat", "Brush hair"] # returns ["wash dog", "Feed cat", "Brush hair"]

# !!!! Moving on from this point in favour of moving through the course

# """
# When an item is marked complete
# the item is removed from view_items
# """
# test_instance = TodoList()
# test_instance.add("Wash dog")
# test_instance.add("Feed cat")
# test_instance.add("Brush hair")
# test_instance.mark_complete ????
# test_instance.view_items() # returns ["wash dog", "Feed cat", "Brush hair"]