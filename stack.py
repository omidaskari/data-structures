# stack.py
"""
Simple stack implementation using a Python list.
This module provides a Stack class with basic operations like push, pop, peek,
and checking if the stack is empty. It raises IndexError on underflow.
"""

class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def is_empty(self) -> bool:
        """Return True if the stack is empty, False otherwise."""
        return len(self.items) == 0

    def push(self, item) -> None:
        """Push an item onto the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.items)
