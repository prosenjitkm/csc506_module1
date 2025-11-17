"""
Service layer - contains business logic
"""
from src.repositories.repository import DataStructureRepository
from src.utils.complexity import get_complexity
from src.utils.logger import get_logger, log_service
import time

# Configure logger
log = get_logger(__name__)


class StackService:
    """Service for Stack operations"""

    def __init__(self, repository):
        self.repository = repository
        log.info("StackService initialized")

    @log_service
    def push(self, value):
        """Push a value to the stack"""
        stack = self.repository.get_stack()
        stack.push(value)
        result = {
            "state": stack.to_list(),
            "size": stack.size()
        }
        log.info(f"Pushed '{value}' to stack, new size: {result['size']}")
        return result

    @log_service
    def pop(self):
        """Pop a value from the stack"""
        stack = self.repository.get_stack()
        if stack.is_empty():
            log.warning("Attempted to pop from empty stack")
            return {"error": "Stack is empty", "state": []}

        value = stack.pop()
        result = {
            "popped": value,
            "state": stack.to_list(),
            "size": stack.size()
        }
        log.info(f"Popped '{value}' from stack, new size: {result['size']}")
        return result

    @log_service
    def get_state(self):
        """Get current stack state"""
        stack = self.repository.get_stack()
        return {
            "state": stack.to_list(),
            "size": stack.size(),
            "is_empty": stack.is_empty()
        }

    @log_service
    def clear(self):
        """Clear the stack"""
        self.repository.reset_stack()
        log.info("Stack cleared")
        return {"state": [], "message": "Stack cleared"}

    @log_service
    def peek(self):
        """Peek at the top element without removing it"""
        stack = self.repository.get_stack()
        if stack.is_empty():
            log.warning("Attempted to peek at empty stack")
            return {"error": "Stack is empty", "value": None}

        value = stack.peek()
        log.info(f"Peeked at stack top: '{value}'")
        return {
            "value": value,
            "state": stack.to_list(),
            "size": stack.size()
        }

    @log_service
    def search(self, value):
        """Search for a value in the stack"""
        stack = self.repository.get_stack()
        index = stack.search(value)

        if index == -1:
            log.info(f"Value '{value}' not found in stack")
            return {
                "found": False,
                "index": -1,
                "message": f"Value '{value}' not found",
                "state": stack.to_list()
            }

        log.info(f"Found value '{value}' at index {index} from top")
        return {
            "found": True,
            "index": index,
            "message": f"Found at position {index} from top",
            "state": stack.to_list(),
            "size": stack.size()
        }


class QueueService:
    """Service for Queue operations"""

    def __init__(self, repository):
        self.repository = repository
        log.info("QueueService initialized")

    @log_service
    def enqueue(self, value):
        """Enqueue a value to the queue"""
        queue = self.repository.get_queue()
        queue.enqueue(value)
        result = {
            "state": queue.to_list(),
            "size": queue.size()
        }
        log.info(f"Enqueued '{value}' to queue, new size: {result['size']}")
        return result

    @log_service
    def dequeue(self):
        """Dequeue a value from the queue"""
        queue = self.repository.get_queue()
        if queue.is_empty():
            log.warning("Attempted to dequeue from empty queue")
            return {"error": "Queue is empty", "state": []}

        value = queue.dequeue()
        result = {
            "dequeued": value,
            "state": queue.to_list(),
            "size": queue.size()
        }
        log.info(f"Dequeued '{value}' from queue, new size: {result['size']}")
        return result

    @log_service
    def get_state(self):
        """Get current queue state"""
        queue = self.repository.get_queue()
        return {
            "state": queue.to_list(),
            "size": queue.size(),
            "is_empty": queue.is_empty()
        }

    @log_service
    def clear(self):
        """Clear the queue"""
        self.repository.reset_queue()
        log.info("Queue cleared")
        return {"state": [], "message": "Queue cleared"}

    @log_service
    def peek(self):
        """Peek at the front element without removing it"""
        queue = self.repository.get_queue()
        if queue.is_empty():
            log.warning("Attempted to peek at empty queue")
            return {"error": "Queue is empty", "value": None}

        value = queue.peek()
        log.info(f"Peeked at queue front: '{value}'")
        return {
            "value": value,
            "state": queue.to_list(),
            "size": queue.size()
        }

    @log_service
    def search(self, value):
        """Search for a value in the queue"""
        queue = self.repository.get_queue()
        index = queue.search(value)

        if index == -1:
            log.info(f"Value '{value}' not found in queue")
            return {
                "found": False,
                "index": -1,
                "message": f"Value '{value}' not found",
                "state": queue.to_list()
            }

        log.info(f"Found value '{value}' at index {index} from front")
        return {
            "found": True,
            "index": index,
            "message": f"Found at position {index} from front",
            "state": queue.to_list(),
            "size": queue.size()
        }


class LinkedListService:
    """Service for LinkedList operations"""

    def __init__(self, repository):
        self.repository = repository
        log.info("LinkedListService initialized")

    @log_service
    def insert(self, value):
        """Insert a value at the head of the linked list"""
        log.info(f"Inserting value '{value}' at head")
        linked_list = self.repository.get_linked_list()
        linked_list.insert_at_head(value)
        result = {
            "state": linked_list.to_list(),
            "size": linked_list.size(),
            "complexity": get_complexity("linked_list", "insert")
        }
        log.info(f"Insert successful. New size: {result['size']}, Complexity: {result['complexity']}")
        return result

    @log_service
    def delete(self, value):
        """Delete a value from the linked list"""
        log.info(f"Attempting to delete value '{value}'")
        linked_list = self.repository.get_linked_list()
        success = linked_list.delete(value)
        result = {
            "deleted": success,
            "state": linked_list.to_list(),
            "size": linked_list.size(),
            "complexity": get_complexity("linked_list", "delete")
        }
        if success:
            log.info(f"Delete successful. New size: {result['size']}, Complexity: {result['complexity']}")
        else:
            log.warning(f"Delete failed - value '{value}' not found")
        return result

    @log_service
    def get_state(self):
        """Get current linked list state"""
        linked_list = self.repository.get_linked_list()
        return {
            "state": linked_list.to_list(),
            "size": linked_list.size(),
            "is_empty": linked_list.is_empty()
        }

    @log_service
    def clear(self):
        """Clear the linked list"""
        self.repository.reset_linked_list()
        log.info("LinkedList cleared")
        return {"state": [], "message": "LinkedList cleared"}

    @log_service
    def search(self, value):
        """Search for a value in the linked list"""
        linked_list = self.repository.get_linked_list()
        index = linked_list.search(value)

        if index == -1:
            log.info(f"Value '{value}' not found in linked list")
            return {
                "found": False,
                "index": -1,
                "message": f"Value '{value}' not found",
                "state": linked_list.to_list()
            }

        log.info(f"Found value '{value}' at index {index}")
        return {
            "found": True,
            "index": index,
            "message": f"Found at position {index}",
            "state": linked_list.to_list(),
            "size": linked_list.size()
        }


class ComplexityService:
    """Service for complexity analysis"""

    def __init__(self):
        log.info("ComplexityService initialized")

    def get_complexity_info(self, data_structure, operation):
        """Get complexity information for an operation"""
        complexity = get_complexity(data_structure, operation)
        log.debug(f"Retrieved complexity for {data_structure}.{operation}: {complexity}")
        return complexity

    def get_detailed_complexity(self, data_structure, operation):
        """Get detailed complexity with time and space"""
        from src.utils.complexity import get_detailed_complexity
        return get_detailed_complexity(data_structure, operation)

    def get_use_cases(self, data_structure):
        """Get use case information for a data structure"""
        from src.utils.complexity import get_use_cases
        use_cases = get_use_cases(data_structure)
        log.debug(f"Retrieved use cases for {data_structure}")
        return use_cases

    def get_all_info(self, data_structure):
        """Get complete information including all complexities and use cases"""
        from src.utils.complexity import get_all_complexities, get_use_cases
        return {
            "complexities": get_all_complexities(data_structure),
            "use_cases": get_use_cases(data_structure)
        }


class BenchmarkService:
    """Service for performance benchmarking"""

    def __init__(self):
        self.test_sizes = [100, 500, 1000, 2000]
        log.info("BenchmarkService initialized")

    @log_service
    def run_benchmark(self, data_structure, operation):
        """Run performance benchmark"""
        from src.models.datastructures import Stack, Queue, LinkedList

        log.info(f"Starting benchmark for {data_structure} - {operation}")
        times = []

        for n in self.test_sizes:
            if data_structure == "stack":
                times.append(self._benchmark_stack(n, operation))
            elif data_structure == "queue":
                times.append(self._benchmark_queue(n, operation))
            elif data_structure == "linked_list":
                times.append(self._benchmark_linked_list(n, operation))
            else:
                log.error(f"Unknown data structure: {data_structure}")
                raise ValueError(f"Unknown data structure: {data_structure}")

        predicted = get_complexity(data_structure, operation)

        result = {
            "sizes": self.test_sizes,
            "times": [round(t, 4) for t in times],
            "predicted": predicted,
            "data_structure": data_structure,
            "operation": operation
        }
        log.info(f"Benchmark complete. Predicted: {predicted}, Times: {result['times']}")
        return result

    def _benchmark_stack(self, size, operation):
        """Benchmark stack operation"""
        from src.models.datastructures import Stack
        s = Stack()

        # Pre-populate for delete and search operations
        if operation in ["delete", "search"]:
            for i in range(size):
                s.push(i)

        start = time.perf_counter()

        if operation == "insert":
            for i in range(size):
                s.push(i)
        elif operation == "delete":
            for i in range(size):
                s.pop()
        elif operation == "search":
            for i in range(size):
                s.search(i % size)  # Search for various values

        end = time.perf_counter()
        elapsed = end - start
        log.debug(f"Stack {operation} benchmark (size={size}): {elapsed:.6f}s")
        return elapsed

    def _benchmark_queue(self, size, operation):
        """Benchmark queue operation"""
        from src.models.datastructures import Queue
        q = Queue()

        # Pre-populate for delete and search operations
        if operation in ["delete", "search"]:
            for i in range(size):
                q.enqueue(i)

        start = time.perf_counter()

        if operation == "insert":
            for i in range(size):
                q.enqueue(i)
        elif operation == "delete":
            for i in range(size):
                q.dequeue()
        elif operation == "search":
            for i in range(size):
                q.search(i % size)  # Search for various values

        end = time.perf_counter()
        elapsed = end - start
        log.debug(f"Queue {operation} benchmark (size={size}): {elapsed:.6f}s")
        return elapsed

    def _benchmark_linked_list(self, size, operation):
        """Benchmark linked list operation"""
        from src.models.datastructures import LinkedList
        ll = LinkedList()

        # Pre-populate for delete and search operations
        if operation in ["delete", "search"]:
            for i in range(size):
                ll.insert_at_head(i)

        start = time.perf_counter()

        if operation == "insert":
            for i in range(size):
                ll.insert_at_head(i)
        elif operation == "delete":
            # Delete from head for consistency
            for i in range(size):
                ll.delete(i)
        elif operation == "search":
            for i in range(size):
                ll.search(i % size)  # Search for various values

        end = time.perf_counter()
        elapsed = end - start
        log.debug(f"LinkedList {operation} benchmark (size={size}): {elapsed:.6f}s")
        return elapsed

