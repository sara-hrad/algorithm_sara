# https://github.com/sara-hrad
# The implementation of a sorting algorithm named as quicksort.
# This algorithm has the average running time of O(n) with no extra memory

# The partition function partition the array to entries smaller and bigger than pivot point.
def partition(array, left, right):
    pivot = array[left]
    i = left+1
    for j in range(i, right+1):
        if array[j] < pivot:
            (array[i], array[j]) = (array[j], array[i])
            i = i + 1

    (array[left], array[i-1]) = (array[i-1], array[left])
    return i-1

# The quicksort sort each part of the partioned array recursively.
def quicksort(array, left, right):
    if left < right:
        partition_idx = partition(array, left, right)
        quicksort(array, left, partition_idx - 1)
        quicksort(array, partition_idx + 1, right)


if __name__ == '__main__':
    array_example = [1, 7, 8, 9, 1, 9]
    n_array = len(array_example)
    quicksort(array_example, 0, n_array-1)
    print('sorted array:')
    print(array_example)

