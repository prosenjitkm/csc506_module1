"""
Controller layer - handles HTTP requests and responses
"""
from flask import request, jsonify
from src.utils.logger import get_logger, log_method

# Get logger for this module
log = get_logger(__name__)


class StackController:
    """Controller for Stack endpoints"""

    def __init__(self, stack_service):
        self.stack_service = stack_service
        log.info("StackController initialized")

    @log_method
    def push(self):
        """Handle push request"""
        data = request.get_json()
        value = data.get("value")

        if value is None or value == "":
            log.warning("Push request rejected - missing value")
            return jsonify({"error": "Value is required"}), 400

        log.info(f"Pushing value: {value}")
        result = self.stack_service.push(value)
        return jsonify(result)

    @log_method
    def pop(self):
        """Handle pop request"""
        result = self.stack_service.pop()

        if "error" in result:
            log.warning(f"Pop request failed: {result['error']}")
            return jsonify(result), 400

        log.info(f"Popped value: {result.get('popped')}")
        return jsonify(result)

    @log_method
    def get_state(self):
        """Handle get state request"""
        result = self.stack_service.get_state()
        log.info(f"Retrieved stack state: size={result.get('size')}")
        return jsonify(result)

    @log_method
    def clear(self):
        """Handle clear request"""
        result = self.stack_service.clear()
        log.info("Stack cleared")
        return jsonify(result)


class QueueController:
    """Controller for Queue endpoints"""

    def __init__(self, queue_service):
        self.queue_service = queue_service
        log.info("QueueController initialized")

    @log_method
    def enqueue(self):
        """Handle enqueue request"""
        data = request.get_json()
        value = data.get("value")

        if value is None or value == "":
            log.warning("Enqueue request rejected - missing value")
            return jsonify({"error": "Value is required"}), 400

        log.info(f"Enqueueing value: {value}")
        result = self.queue_service.enqueue(value)
        return jsonify(result)

    @log_method
    def dequeue(self):
        """Handle dequeue request"""
        result = self.queue_service.dequeue()

        if "error" in result:
            log.warning(f"Dequeue request failed: {result['error']}")
            return jsonify(result), 400

        log.info(f"Dequeued value: {result.get('dequeued')}")
        return jsonify(result)

    @log_method
    def get_state(self):
        """Handle get state request"""
        result = self.queue_service.get_state()
        log.info(f"Retrieved queue state: size={result.get('size')}")
        return jsonify(result)

    @log_method
    def clear(self):
        """Handle clear request"""
        result = self.queue_service.clear()
        log.info("Queue cleared")
        return jsonify(result)


class LinkedListController:
    """Controller for LinkedList endpoints"""

    def __init__(self, linked_list_service):
        self.linked_list_service = linked_list_service
        log.info("LinkedListController initialized")

    @log_method
    def insert(self):
        """Handle insert request"""
        data = request.get_json()
        value = data.get("value")

        if value is None or value == "":
            log.warning("Insert request rejected - missing value")
            return jsonify({"error": "Value is required"}), 400

        log.info(f"Inserting value: {value}")
        result = self.linked_list_service.insert(value)
        return jsonify(result)

    @log_method
    def delete(self):
        """Handle delete request"""
        data = request.get_json()
        value = data.get("value")

        if value is None or value == "":
            log.warning("Delete request rejected - missing value")
            return jsonify({"error": "Value is required"}), 400

        log.info(f"Deleting value: {value}")
        result = self.linked_list_service.delete(value)
        return jsonify(result)

    @log_method
    def get_state(self):
        """Handle get state request"""
        result = self.linked_list_service.get_state()
        log.info(f"Retrieved linked list state: size={result.get('size')}")
        return jsonify(result)

    @log_method
    def clear(self):
        """Handle clear request"""
        result = self.linked_list_service.clear()
        log.info("LinkedList cleared")
        return jsonify(result)


class ComplexityController:
    """Controller for Complexity endpoints"""

    def __init__(self, complexity_service):
        self.complexity_service = complexity_service
        log.info("ComplexityController initialized")

    @log_method
    def get_complexity(self):
        """Handle get complexity request"""
        ds = request.args.get("ds")
        op = request.args.get("op")

        if not ds or not op:
            log.warning("Complexity request rejected - missing parameters")
            return jsonify({"error": "Missing parameters"}), 400

        log.info(f"Getting complexity for: {ds} - {op}")
        complexity = self.complexity_service.get_complexity_info(ds, op)
        return jsonify({"complexity": complexity})


class BenchmarkController:
    """Controller for Benchmark endpoints"""

    def __init__(self, benchmark_service):
        self.benchmark_service = benchmark_service
        log.info("BenchmarkController initialized")

    @log_method
    def run_benchmark(self):
        """Handle benchmark request"""
        ds = request.args.get("ds")
        op = request.args.get("op", "insert")

        if not ds:
            log.warning("Benchmark request rejected - missing data structure")
            return jsonify({"error": "Data structure is required"}), 400

        log.info(f"Running benchmark for: {ds} - {op}")
        try:
            result = self.benchmark_service.run_benchmark(ds, op)
            log.info(f"Benchmark completed successfully for {ds}")
            return jsonify(result)
        except ValueError as e:
            log.error(f"Benchmark failed: {str(e)}")
            return jsonify({"error": str(e)}), 400

