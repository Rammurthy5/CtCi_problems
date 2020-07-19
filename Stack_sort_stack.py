"""
Sort a given stack

"""

from DataStructures.Stack_design import Stack, s


sec_stack = Stack()
# s.print_stack()


def _sort():

    while not s.is_empty():
        temp = s.pop()[1]
        while not sec_stack.is_empty() and sec_stack.peek()[1] > temp:
            s.push(sec_stack.pop()[1])
        sec_stack.push(temp)

    return sec_stack


print(_sort().print_stack())
