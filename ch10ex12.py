""" Exercise 12
Two words “interlock” if taking alternating letters from each forms a new word.
For example, “shoe” and “cold” interlock to form “schooled”.

Solution: http://thinkpython2.com/code/interlock.py.
Credit: This exercise is inspired by an example at http://puzzlers.org.

Write a program that finds all pairs of words that interlock.
Hint: don’t enumerate all pairs!
"""

"""For each word in the word list, determine its two "interlocking" words and
if both of those are in the word list, add to a collection to be returned.."""

from ch10ex10 import listWords2
import pprint

def interlock(word_list, word):
    """Return tuple of the two "interlocking" words found in "word"."""
    return (word[::2], word[1::2])

def interlock_search():
    """If both words are in the word list, add to interlocked_words; return."""
    interlocked_words = []
    words = listWords2()
    for i, word in enumerate(words):
        found_pair = interlock(words, word)
        # Print status every 100 items of original list, to prevent napping.
        if not i % 100:
            print('#{}: {} = {} + {}'.format(i, word, found_pair[0],
                found_pair[1]))
        if found_pair[0] in words and found_pair[1] in words:
            interlocked_words.append(found_pair)
    return interlocked_words

pprint.pprint(interlock_search())
