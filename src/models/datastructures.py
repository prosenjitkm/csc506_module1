"""
Data structure implementations for learning tool
"""


class Stack:
    """Stack implementation using a list"""

    def __init__(self):
        self.items = []

    def push(self, value):
        """Add an element to the top of the stack"""
        self.items.append(value)

    def pop(self):
        """Remove and return the top element from the stack"""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the stack"""
        return len(self.items)

    def search(self, value):
        """Search for a value and return its index from the top (0-based)"""
        try:
            # Find from the end (top of stack)
            reversed_items = list(reversed(self.items))
            return reversed_items.index(value)
        except ValueError:
            return -1

    def to_list(self):
        """Return the stack as a list (bottom to top)"""
        return self.items.copy()


class Queue:
    """Queue implementation using a list"""

    def __init__(self):
        self.items = []

    def enqueue(self, value):
        """Add an element to the rear of the queue"""
        self.items.append(value)

    def dequeue(self):
        """Remove and return the front element from the queue"""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """Return the front element without removing it"""
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the queue"""
        return len(self.items)

    def search(self, value):
        """Search for a value and return its index from the front"""
        try:
            return self.items.index(value)
        except ValueError:
            return -1

    def to_list(self):
        """Return the queue as a list (front to rear)"""
        return self.items.copy()


class Node:
    """Node for linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list implementation"""

    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        """Insert a new node at the head of the list"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        """Insert a new node at the tail of the list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        """Delete the first occurrence of a value"""
        if self.head is None:
            return False

        # If head needs to be deleted
        if self.head.data == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def search(self, value):
        """Search for a value and return its index (0-based)"""
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return -1

    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None

    def size(self):
        """Return the number of nodes in the list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self):
        """Convert the linked list to a Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

