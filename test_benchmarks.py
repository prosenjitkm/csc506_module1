"""
Test benchmark functionality for all operations
"""
from src.services.service import BenchmarkService

def test_benchmarks():
    print("\n" + "="*60)
    print("🧪 TESTING BENCHMARK SERVICE")
    print("="*60)

    benchmark_service = BenchmarkService()

    # Test Stack operations
    print("\n📚 Stack Benchmarks:")
    for operation in ["insert", "delete", "search"]:
        print(f"  Testing {operation}...", end=" ")
        try:
            result = benchmark_service.run_benchmark("stack", operation)
            print(f"✅ {result['predicted']}")
        except Exception as e:
            print(f"❌ Error: {e}")

    # Test Queue operations
    print("\n🎫 Queue Benchmarks:")
    for operation in ["insert", "delete", "search"]:
        print(f"  Testing {operation}...", end=" ")
        try:
            result = benchmark_service.run_benchmark("queue", operation)
            print(f"✅ {result['predicted']}")
        except Exception as e:
            print(f"❌ Error: {e}")

    # Test Linked List operations
    print("\n🔗 Linked List Benchmarks:")
    for operation in ["insert", "delete", "search"]:
        print(f"  Testing {operation}...", end=" ")
        try:
            result = benchmark_service.run_benchmark("linked_list", operation)
            print(f"✅ {result['predicted']}")
        except Exception as e:
            print(f"❌ Error: {e}")

    print("\n" + "="*60)
    print("🎉 ALL BENCHMARK OPERATIONS TESTED!")
    print("="*60)
    print("\n✅ Now you can benchmark:")
    print("   • Insert operations (O(1) for Stack, Queue, Linked List)")
    print("   • Delete operations (O(1) for Stack, O(n) for Queue & LL)")
    print("   • Search operations (O(n) for all structures)")
    print("\n")

if __name__ == "__main__":
    test_benchmarks()

