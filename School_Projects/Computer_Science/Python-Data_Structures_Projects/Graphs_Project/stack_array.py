from typing import *


class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''

    def __init__(self, capacity: int) -> None:
        '''Creates and empty stack with a capacity'''
        self.capacity: int = capacity
        self.items: list[Any] = [None] * capacity
        self.num_items: int = 0

    def is_empty(self) -> bool:
        return self.num_items == 0
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''

    def is_full(self) -> bool:
        return self.num_items == self.capacity
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''

    def push(self, item: Any) -> None:
        if self.is_full():
            raise IndexError('Stack is full')
        self.items[self.num_items] = item
        self.num_items += 1
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('Stack is empty')
        self.num_items -= 1
        popped_item = self.items[self.num_items]
        return popped_item
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError('Stack is empty')
        top_item = self.num_items - 1
        peek_item = self.items[top_item]
        return peek_item

        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''

    def size(self) -> int:
        return self.num_items
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''

