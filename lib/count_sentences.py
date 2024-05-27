#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        self.value = value  

    def get_value(self):
        return self._value

    def set_value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        self._value = value

    value = property(get_value, set_value)

    def is_sentence(self):
        if self._value and self._value[-1] == ".":
            return True
        return False
    
    def is_question(self):
        if self._value and self._value[-1] == "?":
            return True
        return False
    def is_exclamation(self):
        if self._value and self._value[-1] =="!":
            return True
        return False
    def count_sentences(self):
        sentence_pattern = r'[A-Za-z0-9,;\s]+[.!?]'
        sentences = re.findall(sentence_pattern, self._value)
        print(sentences)
        sentences =[s for s in sentences if s.strip()]
        return len(sentences)
