"""
Implement Queue via Stacks
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.dummy = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for i in range(len(self.stack)):
            self.dummy.append(self.stack.pop())
        # popped = self.stack[0]
        # del self.stack[0]
        return self.dummy.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.dummy[-1] if self.dummy else self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stack and not self.dummy:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
