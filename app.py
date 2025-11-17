"""
CSC506 Module 1 - Data Structure Learning Tool
Main application entry point
"""
from flask import Flask, render_template
from src.repositories.repository import DataStructureRepository
from src.services.service import StackService, QueueService, LinkedListService, ComplexityService, BenchmarkService
from src.controllers.controller import StackController, QueueController, LinkedListController, ComplexityController, BenchmarkController
from src.utils.logger import log_api, get_logger

# Initialize logger for this module
log = get_logger(__name__)

# Initialize Flask app
app = Flask(__name__)
log.info("Initializing Flask application...")

# Initialize layers
repository = DataStructureRepository()
log.info("Repository layer initialized")

# Initialize services
stack_service = StackService(repository)
queue_service = QueueService(repository)
linked_list_service = LinkedListService(repository)
complexity_service = ComplexityService()
benchmark_service = BenchmarkService()
log.info("Service layer initialized")

# Initialize controllers
stack_controller = StackController(stack_service)
queue_controller = QueueController(queue_service)
linked_list_controller = LinkedListController(linked_list_service)
complexity_controller = ComplexityController(complexity_service)
benchmark_controller = BenchmarkController(benchmark_service)
log.info("Controller layer initialized")


# Main route
@app.route("/")
def index():
    """Render the main page"""
    log.info("Serving main page")
    return render_template("index.html")


# Stack routes
@app.route("/api/stack/push", methods=["POST"])
@log_api
def stack_push():
    return stack_controller.push()


@app.route("/api/stack/pop", methods=["POST"])
@log_api
def stack_pop():
    return stack_controller.pop()


@app.route("/api/stack/state", methods=["GET"])
@log_api
def stack_state():
    return stack_controller.get_state()


@app.route("/api/stack/clear", methods=["POST"])
@log_api
def stack_clear():
    return stack_controller.clear()


# Queue routes
@app.route("/api/queue/enqueue", methods=["POST"])
@log_api
def queue_enqueue():
    return queue_controller.enqueue()


@app.route("/api/queue/dequeue", methods=["POST"])
@log_api
def queue_dequeue():
    return queue_controller.dequeue()


@app.route("/api/queue/state", methods=["GET"])
@log_api
def queue_state():
    return queue_controller.get_state()


@app.route("/api/queue/clear", methods=["POST"])
@log_api
def queue_clear():
    return queue_controller.clear()


# LinkedList routes
@app.route("/api/linkedlist/insert", methods=["POST"])
@log_api
def linkedlist_insert():
    return linked_list_controller.insert()


@app.route("/api/linkedlist/delete", methods=["POST"])
@log_api
def linkedlist_delete():
    return linked_list_controller.delete()


@app.route("/api/linkedlist/state", methods=["GET"])
@log_api
def linkedlist_state():
    return linked_list_controller.get_state()


@app.route("/api/linkedlist/clear", methods=["POST"])
@log_api
def linkedlist_clear():
    return linked_list_controller.clear()


# Complexity route
@app.route("/api/complexity", methods=["GET"])
@log_api
def complexity():
    return complexity_controller.get_complexity()


# Benchmark route
@app.route("/api/benchmark", methods=["GET"])
@log_api
def benchmark():
    return benchmark_controller.run_benchmark()


if __name__ == "__main__":
    log.info("=" * 80)
    log.info("Starting Flask application in debug mode...")
    log.info("=" * 80)
    app.run(debug=True)



