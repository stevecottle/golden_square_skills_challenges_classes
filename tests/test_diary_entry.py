from lib.diary_entry import *

"""
When given a title string and a contents string
#format can return a formatted entry like: 
"My Title: These are the contents"
"""

def test_format_returns_formatted_title_and_contents():
    test_instance = DiaryEntry("My Title", "These are the contents")
    result = test_instance.format()
    assert result == "My Title: These are the contents"

"""
When given a title string and a contents string
#count_words returns the number of words in the contents string
"""

def test_the_class_returns_the_number_of_words_in_the_contents():
    test_instance = DiaryEntry("My Title", "These are the contents")
    result = test_instance.count_words()
    assert result == 4

"""
When given a title string and a contents string
#reading_time returns the words per minute for the contents at the given words per minute
"""