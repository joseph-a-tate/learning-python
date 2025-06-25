# Create bubble sort recursive
def bubble_sort(arr):
    count = 0
    for i in range(len(arr) -1, 0, -1):
        swapped = False
        for j in range(i):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            print("Hi buddy, bubble sort ended earlier")
            return count
    return count

def merge_sort(arr):
    count = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        count += merge_sort(left_half)
        count += merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            count += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            count += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            count += 1
    return count

arr = [12, 1, 4, 23, 64, 2, 8, 8, 19, 1, 0, 101, 6]
arr2 = [12, 1, 4, 23, 64, 2, 8, 8, 19, 1, 0, 101, 6]
print("unsorted: " + str(arr))
count1 = bubble_sort(arr)
count2 = merge_sort(arr2)
print("bubble sorted: " + str(arr))
print("bubble count: " + str(count1)) 
print("merge sorted: " + str(arr2))
print("merge count: " + str(count2))
