"""
Logging utility for the application - Similar to Lombok's @Log4j
"""
import logging
import functools
import time
from flask import request, jsonify
import json

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - [%(levelname)s] - %(funcName)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def get_logger(name):
    """
    Get a logger instance for a module - Similar to Lombok's @Log4j

    Usage:
        log = get_logger(__name__)
        log.info("Message")
    """
    return logging.getLogger(name)


def log_method(func):
    """
    Decorator to log method entry, exit, and execution time
    Similar to Lombok's @Log annotation

    Usage:
        @log_method
        def my_function(self, arg):
            # function body
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)

        # Log method entry with parameters
        args_repr = [repr(a) for a in args[1:]]  # Skip 'self'
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        logger.info(f">>> Entering {func.__name__}({signature})")

        start_time = time.time()

        try:
            # Execute the function
            result = func(*args, **kwargs)

            # Log successful completion
            execution_time = (time.time() - start_time) * 1000  # Convert to ms
            logger.info(f"<<< Exiting {func.__name__} - Execution time: {execution_time:.2f}ms")

            return result

        except Exception as e:
            # Log errors
            execution_time = (time.time() - start_time) * 1000
            logger.error(f"!!! Exception in {func.__name__} after {execution_time:.2f}ms: {str(e)}", exc_info=True)
            raise

    return wrapper


def log_api(func):
    """
    Decorator to log API requests and responses
    Logs: HTTP method, path, request body, response status, response body

    Usage:
        @app.route("/api/endpoint")
        @log_api
        def endpoint():
            return jsonify({"data": "value"})
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('api')

        # Log incoming request
        logger.info("=" * 80)
        logger.info(f">>> INCOMING REQUEST: {request.method} {request.path}")

        if request.method in ['POST', 'PUT', 'PATCH']:
            try:
                request_data = request.get_json()
                logger.info(f"Request Body: {json.dumps(request_data, indent=2)}")
            except:
                logger.info("Request Body: <Non-JSON data>")

        if request.args:
            logger.info(f"Query Parameters: {dict(request.args)}")

        start_time = time.time()

        try:
            # Execute the endpoint function
            response = func(*args, **kwargs)

            # Log response
            execution_time = (time.time() - start_time) * 1000

            # Extract status code
            if isinstance(response, tuple):
                status_code = response[1] if len(response) > 1 else 200
                response_data = response[0]
            else:
                status_code = 200
                response_data = response

            logger.info(f"<<< RESPONSE: {status_code} - Execution time: {execution_time:.2f}ms")

            # Try to log response body
            try:
                if hasattr(response_data, 'get_json'):
                    body = response_data.get_json()
                    logger.info(f"Response Body: {json.dumps(body, indent=2)}")
                elif hasattr(response_data, 'get_data'):
                    body = response_data.get_data(as_text=True)
                    logger.info(f"Response Body: {body[:500]}")  # Limit to 500 chars
            except:
                logger.info("Response Body: <Could not serialize>")

            logger.info("=" * 80)

            return response

        except Exception as e:
            execution_time = (time.time() - start_time) * 1000
            logger.error(f"!!! API ERROR after {execution_time:.2f}ms: {str(e)}", exc_info=True)
            logger.info("=" * 80)
            raise

    return wrapper


def log_service(func):
    """
    Decorator specifically for service layer methods
    Logs business logic operations with detailed context

    Usage:
        @log_service
        def push(self, value):
            # service logic
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(f"service.{func.__module__}")

        # Get class name if it's a method
        class_name = args[0].__class__.__name__ if args else "Unknown"

        # Log entry
        args_repr = [repr(a) for a in args[1:]][:3]  # First 3 args only
        signature = ", ".join(args_repr)
        logger.info(f"[{class_name}] >>> {func.__name__}({signature})")

        start_time = time.time()

        try:
            result = func(*args, **kwargs)
            execution_time = (time.time() - start_time) * 1000

            # Log result summary
            result_summary = str(result)[:100] if result else "None"
            logger.info(f"[{class_name}] <<< {func.__name__} returned: {result_summary} ({execution_time:.2f}ms)")

            return result

        except Exception as e:
            execution_time = (time.time() - start_time) * 1000
            logger.error(f"[{class_name}] !!! {func.__name__} failed after {execution_time:.2f}ms: {str(e)}")
            raise

    return wrapper


# Pre-configured loggers for each layer
log = get_logger(__name__)  # Default logger
api_log = get_logger('api')
controller_log = get_logger('controller')
service_log = get_logger('service')
repository_log = get_logger('repository')
model_log = get_logger('model')

