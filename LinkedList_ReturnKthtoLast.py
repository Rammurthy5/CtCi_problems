"""
Given a number k, and just return kth number from the last node of LinkedList (singly)

"""


from DataStructures.LinkedList_design import ch


def find_kth(k):

    if k > len(ch) or k < 0:
        print("k value is bigger than length of the LinkedList")
        return False

    if k == len(ch):
        return ch.head.data

    if k == 0:
        return ch.tail.data

    iteration = len(ch)-k
    i = 1
    curr = ch.head
    while i<iteration:
        curr = curr.next
        i+=1

    return curr.data


print(find_kth(3))
print(find_kth(8))
print(find_kth(-5))
print(find_kth(0))
print(find_kth(7))