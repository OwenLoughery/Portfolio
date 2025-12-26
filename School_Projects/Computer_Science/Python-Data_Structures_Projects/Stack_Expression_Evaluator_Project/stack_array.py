from typing import *


class Stack:

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.items: list[Any] = [None] * capacity
        self.num_items: int = 0

    def is_empty(self) -> bool:
        return self.num_items == 0


    def is_full(self) -> bool:
        return self.num_items == self.capacity


    def push(self, item: Any) -> None:
        if self.is_full():
            raise IndexError('Stack is full')
        self.items[self.num_items] = item
        self.num_items += 1


    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('Stack is empty')
        self.num_items -= 1
        popped_item = self.items[self.num_items]
        return popped_item


    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError('Stack is empty')
        top_item = self.num_items - 1
        peek_item = self.items[top_item]
        return peek_item


    def size(self) -> int:
        return self.num_items


