class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.dummy.next == self.dummy

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head end of list) to highest (at tail end of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance, O(1) best-case performance.  Assume that all
           items added to your list can be compared using the < operator and can be compared for equality/inequality using ==.
           Make no other assumptions about the items in your list'''
        c = self.dummy.next
        while c != self.dummy and c.item < item:
            c = c.next
        if c != self.dummy and c.item == item:
            return False
        node = Node(item)
        node.next = c
        node.prev = c.prev
        c.prev.next = node
        c.prev = node
        return True

    def remove_by_value(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list)
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance, O(1) best-case performance'''
        c = self.dummy.next
        while c != self.dummy and c.item < item:
            c = c.next
        if c != self.dummy and c.item == item:
            c.prev.next = c.next
            c.next.prev = c.prev
            return True
        else:
            return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance, O(1) best-case performance'''
        c = self.dummy.next
        index = 0
        while c != self.dummy and c.item < item:
            c = c.next
            index += 1
        if c != self.dummy and c.item == item:
            return index
        else:
            return None

    def remove_by_index(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance, O(1) best-case performance'''
        if index < 0 or index >= self.size():
            raise IndexError('Index not in list')
        c = self.dummy.next
        c_index = 0
        while c != self.dummy and c_index < index:
            c = c.next
            c_index += 1
        if c == self.dummy:
            raise IndexError
        c.prev.next = c.next
        c.next.prev = c.prev
        return c.item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance, O(1) best-case performance'''
        return self.search_helper(self.dummy.next, item)

    def search_helper(self, node, item):
        if node is self.dummy:
            return False
        elif node.item == item:
            return True
        return self.search_helper(node.next, item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        result = []
        c = self.dummy.next
        while c != self.dummy:
            result.append(c.item)
            c = c.next
        return result

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.python_list_reversed_helper(self.dummy.prev)

    def python_list_reversed_helper(self, node):
        if node is self.dummy:
            return []
        return [node.item] + self.python_list_reversed_helper(node.prev)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.dummy.next)
    def size_helper(self, node):
        if node is self.dummy:
            return 0
        return 1 + self.size_helper(node.next)
