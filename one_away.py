"""
Given two strings, verify if there is one or zero insert / del / alter.
"""

def isAltered(a: str, b: str) -> bool:

    if not -2<len(a)-len(b)<2:
        return False

    alter = 0
    L=len(b)
    if len(a)<len(b):
        L=len(a)


    for i in range(L):
        if a[i] != b[i]:
            alter+=1

        if alter>2:
            print(False)
            return
        if alter==2 and len(a)==len(b):
            print(False)
            return


    print(True)
    return

isAltered("pale", "pse")
