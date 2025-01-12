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

arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print("Original Array: ", arr)
print("Sorted Array: ", insertion_sort(arr))
'''
Expected Output:
Enter number of elements : 5
12
11
13
5
6
Original Array:  [12, 11, 13, 5, 6]
Sorted Array:  [13, 12, 11, 6, 5]
'''