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
When given an integer which represents 
the number of words-per-minute (wpm) which a user can read
#reading_time returns an estimate of the reading time in 
minutes for the contents at the given wpm
"""

def test_class_returns_word_per_minute():
    test_instance = DiaryEntry("My Title", "one two three four five six")
    result = test_instance.reading_time(2)
    assert result == 3

# """
# !!!!!!! I got lost at this point
# When given a contents of eighteen words and
# a wpm of 2
# #reading_chink returns the first six words
# """

# def test_calss_returns_chunk_readable_in_given_number_of_mins():
#     test_instance = DiaryEntry("Title name", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen")
#     result = test_instance.reading_chunk(2, 3)
#     assert result == "one two three four five six"