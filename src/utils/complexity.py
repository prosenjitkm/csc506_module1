"""
Complexity information for data structures
Includes time complexity, space complexity, and use case demonstrations
"""

# Comprehensive complexity data with time, space, and use cases
COMPLEXITY_DATA = {
    "stack": {
        "insert": {
            "time": "O(1)",
            "space": "O(1)",
            "explanation": "Push adds to top instantly",
            "details": "Adding to the end of a dynamic array takes constant time (amortized)"
        },
        "delete": {
            "time": "O(1)",
            "space": "O(1)",
            "explanation": "Pop removes from top instantly",
            "details": "Removing from the end of an array takes constant time"
        },
        "search": {
            "time": "O(n)",
            "space": "O(1)",
            "explanation": "Must check each element",
            "details": "Need to traverse the entire stack to find an element"
        }
    },
    "queue": {
        "insert": {
            "time": "O(1)",
            "space": "O(1)",
            "explanation": "Enqueue adds to rear instantly",
            "details": "Adding to the end of a list takes constant time"
        },
        "delete": {
            "time": "O(n)",
            "space": "O(1)",
            "explanation": "Dequeue removes from front (shifts elements)",
            "details": "Removing from the front requires shifting all remaining elements"
        },
        "search": {
            "time": "O(n)",
            "space": "O(1)",
            "explanation": "Must check each element",
            "details": "Need to traverse the queue to find an element"
        }
    },
    "linked_list": {
        "insert": {
            "time": "O(1)",
            "space": "O(1)",
            "explanation": "Insert at head instantly",
            "details": "Only need to update head pointer and new node's next reference"
        },
        "delete": {
            "time": "O(n)",
            "space": "O(1)",
            "explanation": "Must find element first",
            "details": "Need to traverse the list to find and remove the element"
        },
        "search": {
            "time": "O(n)",
            "space": "O(1)",
            "explanation": "Must check each node",
            "details": "Need to traverse the linked list node by node"
        }
    }
}

# Use case information for when to use each data structure
USE_CASES = {
    "stack": {
        "name": "Stack (LIFO - Last In, First Out)",
        "best_for": [
            "Undo/Redo functionality in text editors",
            "Browser back/forward navigation",
            "Function call stack in programming languages",
            "Expression evaluation (e.g., converting infix to postfix)",
            "Backtracking algorithms (e.g., maze solving)",
            "Depth-First Search (DFS) traversal"
        ],
        "real_world_examples": [
            "Stack of plates in a cafeteria",
            "Browser history navigation",
            "Ctrl+Z / Ctrl+Y operations"
        ],
        "advantages": [
            "Fast insertion and deletion at one end (O(1))",
            "Simple implementation",
            "Memory efficient for LIFO operations"
        ],
        "disadvantages": [
            "No random access to elements",
            "Search requires O(n) time",
            "Can only access top element directly"
        ],
        "when_to_use": "When you need Last-In-First-Out access pattern, such as tracking history or managing recursive calls"
    },
    "queue": {
        "name": "Queue (FIFO - First In, First Out)",
        "best_for": [
            "Task scheduling in operating systems",
            "Print job management in printers",
            "Breadth-First Search (BFS) traversal",
            "Request handling in web servers",
            "Message queues in distributed systems",
            "Buffering data streams"
        ],
        "real_world_examples": [
            "Line of customers at a store",
            "Print queue for documents",
            "Call center queue system"
        ],
        "advantages": [
            "Fast insertion at rear (O(1))",
            "Fair processing (first come, first served)",
            "Good for buffering and scheduling"
        ],
        "disadvantages": [
            "Slow deletion from front with array (O(n))",
            "No random access to elements",
            "Search requires O(n) time"
        ],
        "when_to_use": "When you need First-In-First-Out access pattern, such as task scheduling or order processing"
    },
    "linked_list": {
        "name": "Linked List (Dynamic Node-Based Structure)",
        "best_for": [
            "Dynamic memory allocation (size changes frequently)",
            "Implementing other data structures (stacks, queues)",
            "Music or video playlists",
            "Image viewer (previous/next navigation)",
            "Memory management in operating systems",
            "Polynomial manipulation"
        ],
        "real_world_examples": [
            "Music playlist with next/previous buttons",
            "Train cars connected together",
            "Chain of paperclips"
        ],
        "advantages": [
            "Fast insertion/deletion at head (O(1))",
            "Dynamic size (grows and shrinks easily)",
            "No wasted memory from pre-allocation",
            "Easy to insert in the middle"
        ],
        "disadvantages": [
            "No random access (must traverse from head)",
            "Extra memory for storing pointers",
            "Search and tail operations are O(n)",
            "Not cache-friendly (nodes scattered in memory)"
        ],
        "when_to_use": "When you need dynamic size with frequent insertions/deletions, and don't need random access"
    }
}


def get_complexity(data_structure, operation):
    """
    Get the complexity for an operation (backward compatible)
    Returns: String with time complexity and explanation
    """
    if data_structure in COMPLEXITY_DATA and operation in COMPLEXITY_DATA[data_structure]:
        data = COMPLEXITY_DATA[data_structure][operation]
        return f"{data['time']} - {data['explanation']}"
    return "Unknown"


def get_detailed_complexity(data_structure, operation):
    """
    Get detailed complexity information including time and space
    Returns: Dictionary with time, space, explanation, and details
    """
    if data_structure in COMPLEXITY_DATA and operation in COMPLEXITY_DATA[data_structure]:
        return COMPLEXITY_DATA[data_structure][operation]
    return {
        "time": "Unknown",
        "space": "Unknown",
        "explanation": "No data available",
        "details": "This operation is not documented"
    }


def get_use_cases(data_structure):
    """
    Get use case information for a data structure
    Returns: Dictionary with name, best_for, examples, advantages, disadvantages
    """
    if data_structure in USE_CASES:
        return USE_CASES[data_structure]
    return {
        "name": "Unknown",
        "best_for": [],
        "real_world_examples": [],
        "advantages": [],
        "disadvantages": [],
        "when_to_use": "No information available"
    }


def get_all_complexities(data_structure):
    """
    Get all complexity information for a data structure
    Returns: Dictionary with all operations and their complexities
    """
    if data_structure in COMPLEXITY_DATA:
        return COMPLEXITY_DATA[data_structure]
    return {}



