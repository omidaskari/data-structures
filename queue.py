# queue.py
"""
Simple queue implementation using a Python list.
This module provides a Queue class with basic operations like enqueue, dequeue,
and checking if the queue is empty. It raises IndexError on underflow.
"""

class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        return len(self.items) == 0

    def enqueue(self, item) -> None:
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the front item without removing it. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self.items)
