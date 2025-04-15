from lib.grammar_stats import *


# !!! This test is invalid because we don't 
# """
# given an empty string
# #check can return the empty string
# """
# 
# def test_check_returns_an_empty_string():
#     test_instance = GrammarStats()
#     test_instance.check("")
#     result = ""
#     assert result == ""
# 
# 
# unltimately want the method to return a string
# """
# given an multi word string
# #check can return the given string
# """
# def test_check_can_return_multi_word_string():
#     test_instance = GrammarStats()
#     result = test_instance.check("test string")
#     assert result == "test string"

"""
Given a string with a capital at the beginning 
and a '.' at the end #check will return True
"""
def test_check_returns_true_for_capital_at_beginning_and_full_stop_at_end():
    test_instance = GrammarStats()
    result = test_instance.check("T.")
    assert result == True

"""
Given a string with no capital at the beginning 
and a '.' at the end #check will return False
"""
def test_check_returns_false_for_no_capital_at_beginning_and_full_stop_at_end():
    test_instance = GrammarStats()
    result = test_instance.check("t.")
    assert result == False

"""
Given a string with a capital at the beginning 
and a no punctuation at the end #check will return False
"""
def test_check_returns_false_for_no_capital_at_beginning_and_no_punctuation_at_end():
    test_instance = GrammarStats()
    result = test_instance.check("tp")
    assert result == False

"""
Given a string with a capital at the beginning 
and a ',' at the end #check will return True
"""
def test_check_returns_true_for_capital_at_beginning_and_comma_at_end():
    test_instance = GrammarStats()
    result = test_instance.check("T:")
    assert result == True

"""
Given a string with a capital at the beginning 
and a '?' at the end #check will return True
"""
def test_check_returns_true_for_capital_at_beginning_and_question_mark_at_end():
    test_instance = GrammarStats()
    result = test_instance.check("T?")
    assert result == True

"""
Given a string with a capital at the beginning 
and a '!' at the end #check will return True
"""
def test_check_returns_true_for_capital_at_beginning_and_exclamation_mark_at_end():
    test_instance = GrammarStats()
    result = test_instance.check("T!")
    assert result == True


"""
Given a string with a capital at the beginning 
and a '!' at the end #check will return True
"""
def test_check_returns_true_for_capital_at_beginning_and_exclamation_mark_at_end():
    test_instance = GrammarStats()
    result = test_instance.check("T!")
    assert result == True

"""
Given the #check method result is True
#percentage_good will return 100
"""
def test_percentage_good_returns_100_when_check_is_true():
    test_instance = GrammarStats() #create test instance
    test_instance.check("T?") #pass #check a valid string
    result = test_instance.percentage_good() #result is 100 with 1 valid string from #check
    assert result == 100

"""
Given the #check method result is False
#percentage_good will return 0
"""
def test_percentage_good_returns_0_when_check_is_flase():
    test_instance = GrammarStats() #create test instance
    test_instance.check("gdv") #pass #check a valid string
    result = test_instance.percentage_good() #result is 0 with 0 valid string from #check
    assert result == 0

"""
Given two #check methods results are True
#percentage_good will return 100
"""
def test_percentage_good_returns_100_when_two_checks_are_True():
    test_instance = GrammarStats() #create test instance
    test_instance.check("W?") #pass #check a valid string
    test_instance.check("T.") #pass #check another valid string
    result = test_instance.percentage_good() #result is 0 with 0 valid string from #check
    assert result == 100