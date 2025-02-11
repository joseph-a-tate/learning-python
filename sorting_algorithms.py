# Create bubble sort recursive
def bubble_sort(arr):
    for i in range(len(arr) -1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [12, 1, 4, 23, 64, 2, 8, 8, 19, 1, 0, 101, 6]
print("unsorted: " + str(arr))
bubble_sort(arr)
print("sorted: " + str(arr))
