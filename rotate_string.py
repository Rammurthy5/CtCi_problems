def rotateString( A: str, B: str) -> bool:
    if len(A) != len(B):
        return False
    temp = str()
    i = 0


    while i != len(A):
        if A[i] == B[0]:
            if A[i:]==B[:len(A)-i] and temp == B[len(A) - i:]:
                print(True)
                return
        # print(i)
        temp += A[i]
        i += 1
    # import pdb; pdb.set_trace()
    # if A[i:] == B[:len(A) - i] and temp == B[len(A) - i:]:
    #     print( True)
    #     return
    print( False)


rotateString("bbbacddceeb", "ceebbbbacdd")
rotateString("abcde", "cdeab")
