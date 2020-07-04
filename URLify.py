"""
Given a string, replace the white spaces with %20
"""


def urlify(a: str) -> str:
    a = bytearray(a, encoding='utf-8')
    b=str()
    for x in a:
        if x==32:           # 32 is the ord(' ') for whitespace
            b+="%20"
            continue
        b+=chr(x)

    print(b)

urlify("my dog has been named pluto!!!")

