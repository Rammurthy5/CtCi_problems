"""
Given a string, find if there is a palindrome present in its permutations
"""

from itertools import permutations


def isPalindrome(a: str)-> bool:

    b = [''.join(x) for x in permutations(a.replace(" ", ""))]

    for i in b:
        if i==i[::-1]:
            print(True)
            return

    print(False)


isPalindrome("tact coa")
isPalindrome("text")
isPalindrome("Kadvul")
isPalindrome("Heyyy")