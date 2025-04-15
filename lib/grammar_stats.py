


class GrammarStats:
    def __init__(self):
        self.good_checks_exist = False #<-- This is a memory-box for if good checks exist

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if (text[0].isupper()) and (text.endswith((".", ":", "?", "!"))): #<-- If the string matches the requirements ...
            self.good_checks_exist = True # ... change the memory box to True ...
            return True # ... and return True
        else:
            return False

    def percentage_good(self):
        # Returns True:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.

        if self.good_checks_exist == True: # <--- If the memory box is set to true ...
            return 100 # ... return 100 ...
        else: # ... or else ...
            return 0 # ... return 0



instance_one = GrammarStats()
print(f"check: {instance_one.check('Pigasdfdodsygt.')}")
print(f"percentage good: {instance_one.percentage_good()}")
# print(f"check(text): {text}") #<--- Not working

#!!! Leaving unfinished