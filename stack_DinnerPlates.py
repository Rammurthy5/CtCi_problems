"""
Solve stack of stacks. Write a method popAt to pop at given indexed stack from the list of stacks

"""

import heapq


class DinnerPlates:

    def __init__(self, capacity):
        self.stacks = []
        self.cap = capacity
        self.non_full = []  # to record the next to-push stack
        self.non_empty = []  # to record the next to-pop stack

    def push(self, val):
        if self.non_full:
            index = self.non_full[0]
            self.stacks[index] += [val]
            # remove the full stack index
            if len(self.stacks[index]) == self.cap:
                heapq.heappop(self.non_full)
        else:
            index = len(self.stacks)
            heapq.heappush(self.non_full, index)
            heapq.heappush(self.non_empty, -index)
            self.stacks += [[val]]

    def pop(self):
        # NOTE: remove the empty stack indices before we pop.
        while self.non_empty and not self.stacks[-self.non_empty[0]]:
            heapq.heappop(self.non_empty)

        if self.non_empty:
            index = -self.non_empty[0]
            return self.popAtStack(index)
        return -1

    def popAtStack(self, index):
        if self.stacks[index]:
            if len(self.stacks[index]) == self.cap:
                heapq.heappush(self.non_full, index)
            return self.stacks[index].pop()
        return -1
