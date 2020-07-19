"""
An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis.
 People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
 or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data structures to maintain this system and
implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.
"""

# Two Queue via LinkedList implementation

import time

from DataStructures.Queue_design import Queue

# dog_q = Queue()
# cat_q = Queue()
#
#
# def dequeAny():
#     if dog_q.peek()[1] < cat_q.peek()[1]:
#         return dequeDog()
#     return dequeCat()
#
#
# def dequeDog():
#     return dog_q.remove()[0]
#
#
# def dequeCat():
#     return cat_q.remove()[0]
#
#
# def enqueue(data):
#     if 'dog' in data:
#         dog_q.add((data, time.time()))
#         return
#     cat_q.add((data, time.time()))
#     return
#
#
# enqueue('dog1')
# enqueue('dog2')
# enqueue('dog3')
# enqueue('cat1')
# enqueue('dog4')
# enqueue('dog5')
# enqueue('cat2')
#
#
# print(dequeCat())
# print(dequeAny())
# print(dequeDog())


# single queue impleentation
shelter = Queue()


def enque(data):
    shelter.add(data)


def deque_any():
    return shelter.remove()


def deque_dog():
    curr_item = shelter.top

    while not curr_item.next is None:
        if 'dog' in curr_item.data[1]:
            return curr_item.data[0]
        curr_item = curr_item.next

    if 'dog' in curr_item.data[1]:
        return curr_item.data[0]
    else:
        return "No Dogs available"


def deque_cat():
    curr_item = shelter.top

    while not curr_item.next is None:
        if 'cat' in curr_item.data[1]:
            return curr_item.data[0]
        curr_item = curr_item.next

    if 'cat' in curr_item.data[1]:
        return curr_item.data[0]
    else:
        return "No cats available"


enque(('a', 'dog1'))
enque(('b', 'dog2'))
enque(('c', 'dog3'))
enque(('d', 'cat1'))
enque(('e', 'dog4'))
enque(('f', 'dog5'))
enque(('g', 'cat2'))

print(deque_cat())
print(deque_any())
print(deque_dog())
