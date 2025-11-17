"""
Quick test script to verify all operations work correctly
"""
from src.models.datastructures import Stack, Queue, LinkedList

def test_stack():
    print("\n" + "="*50)
    print("TESTING STACK")
    print("="*50)

    s = Stack()

    # Test push
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"✅ Push operations: {s.to_list()}")

    # Test peek
    top = s.peek()
    print(f"✅ Peek (should be 30): {top}")
    assert top == 30, "Peek failed"

    # Test search
    index = s.search(20)
    print(f"✅ Search for 20 (should be at index 1 from top): {index}")
    assert index == 1, "Search failed"

    # Test pop
    popped = s.pop()
    print(f"✅ Pop (should be 30): {popped}")
    assert popped == 30, "Pop failed"

    print("✅ Stack: ALL TESTS PASSED!")

def test_queue():
    print("\n" + "="*50)
    print("TESTING QUEUE")
    print("="*50)

    q = Queue()

    # Test enqueue
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(f"✅ Enqueue operations: {q.to_list()}")

    # Test peek
    front = q.peek()
    print(f"✅ Peek (should be A): {front}")
    assert front == "A", "Peek failed"

    # Test search
    index = q.search("B")
    print(f"✅ Search for B (should be at index 1): {index}")
    assert index == 1, "Search failed"

    # Test dequeue
    dequeued = q.dequeue()
    print(f"✅ Dequeue (should be A): {dequeued}")
    assert dequeued == "A", "Dequeue failed"

    print("✅ Queue: ALL TESTS PASSED!")

def test_linked_list():
    print("\n" + "="*50)
    print("TESTING LINKED LIST")
    print("="*50)

    ll = LinkedList()

    # Test insert
    ll.insert_at_head(100)
    ll.insert_at_head(200)
    ll.insert_at_head(300)
    print(f"✅ Insert operations: {ll.to_list()}")

    # Test search
    index = ll.search(200)
    print(f"✅ Search for 200 (should be at index 1): {index}")
    assert index == 1, "Search failed"

    # Test delete
    success = ll.delete(200)
    print(f"✅ Delete 200 (should be True): {success}")
    assert success == True, "Delete failed"
    print(f"   After delete: {ll.to_list()}")

    # Test search for non-existing
    index = ll.search(999)
    print(f"✅ Search for 999 (should be -1): {index}")
    assert index == -1, "Search for non-existing failed"

    print("✅ Linked List: ALL TESTS PASSED!")

if __name__ == "__main__":
    print("\n" + "🧪 RUNNING DATA STRUCTURE TESTS")
    print("="*50)

    try:
        test_stack()
        test_queue()
        test_linked_list()

        print("\n" + "="*50)
        print("🎉 ALL TESTS PASSED SUCCESSFULLY!")
        print("="*50)
        print("\n✅ The application is ready to use!")
        print("✅ Run 'python app.py' to start the web interface")
        print("\n")

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

