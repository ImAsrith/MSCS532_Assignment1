#Insertion Sort Program
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:#Changed < to > for Descending Order
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 13, 5, 6]
print("Original Array: ", arr)
print("Sorted Array: ", insertion_sort(arr))
#Expected Output: [13, 12, 11, 6, 5]