""" Exercise 11
Two words are a “reverse pair” if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list.
 Solution: http://thinkpython2.com/code/reverse_pair.py. """

import bisect
from ch10ex10 import listWords2

def reverse_pair():
    word_list = listWords2()
    word_set = set(word_list)
    pairs = list()
    for word in word_list:
        # Let's not distinguish differently capitalized forms.
        word = word.lower()

        # We don't want to add the same pair twice, in reverse order.
        # And palindromes don't count, so do this step before anything else.
        word_set.remove(word)
        
        # Reverse word and check for its presence in word_set.
        reversed_word = word[::-1]
        if reversed_word in word_set:
            pairs.append((word, reversed_word))
    
    for pair in pairs:
        print(pair)

reverse_pair()