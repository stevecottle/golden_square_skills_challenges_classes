# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

# class Reminder:
#     # User-facing properties:
#     #   name: string

#     def __init__(self, name):
#         # Parameters:
#         #   name: string
#         # Side effects:
#         #   Sets the name property of the self object
#         pass # No code here yet

#     def remind_me_to(self, task):
#         # Parameters:
#         #   task: string representing a single task
#         # Returns:
#         #   Nothing
#         # Side-effects
#         #   Saves the task to the self object
#         pass # No code here yet

#     def remind(self):
#         # Returns:
#         #   A string reminding the user to do the task
#         # Side-effects:
#         #   Throws an exception if no task is set
#         pass # No code here yet

"""
Actions:
Add todo items to a list
View list
Mark tasks as complete
Have 'complete' tasks disappear
"""

class TodoList():
    def add(self, item):
        #Parameters:
        # item: string
        pass

    def view_items(self):
        # Returns:
        #  list of items
        pass

    def mark_complete(self):
        # Parameters:
        #  item: boolean 
        #       marked complete = True
        #       not marked complete = False
        pass



```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
No tasks to start with
"""
test_instance = TodoList()
test_instance.view_items() # returns []

"""
When a item is added
the item is added to items_list
"""
test_instance = TodoList()
test_instance.add("Wash dog")
test_instance.view_items() # returns ["wash dog"]

"""
When multiple item are added
the items are added to items_list
"""
test_instance = TodoList()
test_instance.add("Wash dog")
test_instance.add("Feed cat")
test_instance.add("Brush hair")
test_instance.view_items() # returns ["wash dog", "Feed cat", "Brush hair"]

"""
When an item is marked complete
the item is removed from view_items
"""
test_instance = TodoList()
test_instance.add("Wash dog")
test_instance.add("Feed cat")
test_instance.add("Brush hair")
test_instance.mark_complete ????
test_instance.view_items() # returns ["wash dog", "Feed cat", "Brush hair"]

## EXAMPLE

# """
# Given a name and a task
# #remind reminds the user to do the task
# """
# reminder = Reminder("Kay")
# reminder.remind_me_to("Walk the dog")
# reminder.remind() # => "Walk the dog, Kay!"

# """
# Given a name and no task
# #remind raises an exception
# """
# reminder = Reminder("Kay")
# reminder.remind() # raises an error with the message "No task set."

# """
# Given a name and an empty task
# #remind still reminds the user to do the task, even though it looks odd
# """
# reminder = Reminder("Kay")
# reminder.remind_me_to("")
# reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
