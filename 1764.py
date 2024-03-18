import sys

if __name__ == "__main__":
    n1, n2 = map(int, sys.stdin.readline().split())

    heap = {}
    result = []

    for _ in range(n1):
        heap[sys.stdin.readline().rstrip("\n")] = 0
    
    len = 0
    key = heap.keys()
    for _ in range(n2):
        data = sys.stdin.readline().rstrip("\n")
        if data in key:
            heap[data] = 1
            len += 1

    heap_sort = sorted(heap.items())

    print(len)
    for (key, value) in heap_sort:
        if value == 1:
            print(key)