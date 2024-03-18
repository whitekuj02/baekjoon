import heapq
import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline())

    heap = []
    for _ in range(num):
        data = int(sys.stdin.readline())
        if data == 0 and len(heap) == 0:
            print(0)
            continue
        elif data == 0 :
            print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, data)
