"""
Given a string, compress it and return. if the compressed is of same length as original, return original
"""


def compress(a: str)->str:
    d = {}
    if len(set(a)) >= len(a)//2:
        print(a)
        return

    for i in a:
        d[i]= d.get(i, 0)+1

    a=str()

    for k,v in d.items():
        a=a+k+str(v)

    print(a)
    return

compress("aaabbbbeee")
compress("abcde")
compress("aabcccccaaa")
