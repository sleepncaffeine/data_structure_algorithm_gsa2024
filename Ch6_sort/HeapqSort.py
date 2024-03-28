import heapq

arr = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 21, 31, 22, 44, 17, 20]
print("Before sort:\t", arr)

heapq.heapify(arr)
print("Heap:\t\t", arr)

sorted_arr = []
while arr:
    sorted_arr.append(heapq.heappop(arr))
print("After sort:\t", sorted_arr)
