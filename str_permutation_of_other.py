"""
Give 2 string, find if one is permutation of other.

"""

# Approach 1 -- counting on a dict

def isPermute(a: str, b: str) -> bool:
    di = dict()

    for x in a:
        di[x] = di.get(x, 0)+1

    for x in b:
        try:
            di[x]-=1
        except:
            return False

    for k, v in di.items():
        if v!=0:
            return False

    return True


print(isPermute("aa", "ab"))
print(isPermute("ba", "ab"))
print(isPermute("aba", "aab"))
print(isPermute("", "ab"))
print(isPermute("a", "ab"))



# Approach 2 - sorting the string and then match the characters.






