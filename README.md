# Data Structures

This repository contains simple implementations of fundamental data structures in Python. Each module defines a class with typical operations.

## Implementations

- **`stack.py`** – Implementation of a Last-In–First-Out (LIFO) stack using a list. Supports push, pop, peek, size, and `is_empty` operations.
- **`queue.py`** – Implementation of a First-In–First-Out (FIFO) queue using a list. Supports enqueue, dequeue, peek, size, and `is_empty` operations.

## Usage

You can import these classes in your Python projects or run simple tests in an interactive session. For example:

```python
from stack import Stack

s = Stack()
s.push(1)
s.push(2)
print(s.pop())  # Outputs 2
```

Similar usage applies to the `Queue` class:

```python
from queue import Queue

q = Queue()
q.enqueue('a')
q.enqueue('b')
print(q.dequeue())  # Outputs 'a'
```

## Notes

These implementations are intentionally basic and designed for educational purposes. They do not include thread safety or advanced features. Feel free to extend them or add additional data structures such as linked lists, binary trees, or hash tables.
