"""
Intro to python exercises shell code
"""

def is_odd(x):
    if (x % 2 == 0):
        return False
    else:
        return True
    """
    returns True if x is odd and False otherwise
    """


def is_palindrome(word):
    for c in range(0, len(word)/2):
        if word[c] != word[len(word)-c]:
            return False:
    return True
    """
    returns whether `word` is spelled the same forwards and backwards
    """


def only_odds(numlist):
    for num in numlist:
        if num % 2 != 0:
            numlist.remove(numlist[num])
    return numlist
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """


def count_words(text):
    dictionary = {}
    words = text.split()
    for word in words:
        if word in dictionary:
            dictionary.update({word: (dictionary[word]+1)}
        else:
            dictionary.update({word: 1})
    return dictionary
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
