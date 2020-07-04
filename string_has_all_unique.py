"""
Determine if given string has all unqiue characters

"""


def isUnique(s: str) -> str:
    d = set()

    for char in s:
        d.add(char)

    if len(d) == len(s):
        print(True)
        return
    print(False)
    return

isUnique("Hey")
isUnique("Hhy")
isUnique("HEy")
isUnique("121y")
isUnique("Oo")
