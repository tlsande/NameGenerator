from random import *

def printArr(arr, n) :
    for i in range(0, n) :
        if(i == 0) :
            print(arr[i], end='')
        else:
            print(", ", test[i], end='')
    print("\n")

def partition(arr, low, high):
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if(arr[j] <= pivot):
            arr[j],arr[i] = arr[i],arr[j]
            i += 1

    arr[i],arr[high] = arr[high],arr[i]
    return i

def quickSort(arr, lower, upper) :
    if(lower < upper) :
        m = partition(arr, lower, upper)

        quickSort(arr, lower, m - 1)
        quickSort(arr, m + 1, upper)

n = 20
test = [0] * n

for i in range(0, n) :
    test[i] = randint(0, 100)

print("Unsorted array:")
printArr(test, n)

print("Sorted array:")
quickSort(test, 0, n - 1)
printArr(test, n)


