"""
Implement three stacks from single array

"""

from typing import List
from DataStructures.Stack_design import Stack


def implement_stack(arr: List) -> Stack:
    s = Stack()
    for i in arr:
        s.push(i)

    return s


def convert_array_stack(arr: List, n: int) -> Stack:
    if n==1:
        return implement_stack(arr)

    q, r = divmod(len(arr), n)
    result = []
    k = q
    j=0
    for _ in range(1, n):
        result.append(implement_stack(arr[j:k]))
        j = k
        k+=q
    result.append(implement_stack(arr[j::]))

    return result


result = convert_array_stack([1,2,3,4,5,6,7,8,9], 5)
for i in result:
    print(i)
    print(i.print_stack())

