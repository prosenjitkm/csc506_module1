"""
Repository layer - handles data storage and retrieval
"""
from src.models.datastructures import Stack, Queue, LinkedList
from src.utils.logger import get_logger

# Get logger for this module
log = get_logger(__name__)


class DataStructureRepository:
    """Repository for managing data structure instances"""

    def __init__(self):
        self._stack = Stack()
        self._queue = Queue()
        self._linked_list = LinkedList()
        log.info("DataStructureRepository initialized with empty data structures")

    # Stack repository methods
    def get_stack(self):
        """Get the stack instance"""
        log.debug("Retrieved stack instance")
        return self._stack

    def reset_stack(self):
        """Reset the stack to empty state"""
        self._stack = Stack()
        log.info("Stack reset to empty state")
        return self._stack

    # Queue repository methods
    def get_queue(self):
        """Get the queue instance"""
        log.debug("Retrieved queue instance")
        return self._queue

    def reset_queue(self):
        """Reset the queue to empty state"""
        self._queue = Queue()
        log.info("Queue reset to empty state")
        return self._queue

    # LinkedList repository methods
    def get_linked_list(self):
        """Get the linked list instance"""
        log.debug("Retrieved linked list instance")
        return self._linked_list

    def reset_linked_list(self):
        """Reset the linked list to empty state"""
        self._linked_list = LinkedList()
        log.info("LinkedList reset to empty state")
        return self._linked_list

