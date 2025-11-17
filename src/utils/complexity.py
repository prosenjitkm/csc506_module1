"""
Complexity information for data structures
"""

# Simple complexity data for each data structure
COMPLEXITY_DATA = {
    "stack": {
        "insert": "O(1) - Push adds to top instantly",
        "delete": "O(1) - Pop removes from top instantly",
        "search": "O(n) - Must check each element"
    },
    "queue": {
        "insert": "O(1) - Enqueue adds to rear instantly",
        "delete": "O(n) - Dequeue removes from front (shifts elements)",
        "search": "O(n) - Must check each element"
    },
    "linked_list": {
        "insert": "O(1) - Insert at head instantly",
        "delete": "O(n) - Must find element first",
        "search": "O(n) - Must check each node"
    }
}


def get_complexity(data_structure, operation):
    """Get the complexity for an operation"""
    if data_structure in COMPLEXITY_DATA and operation in COMPLEXITY_DATA[data_structure]:
        return COMPLEXITY_DATA[data_structure][operation]
    return "Unknown"


