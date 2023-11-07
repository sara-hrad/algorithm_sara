def partition(array, left, right):
    pivot = array[left]
    i = left+1
    for j in range(i, right+1):
        if array[j] < pivot:
            (array[i], array[j]) = (array[j], array[i])
            i = i + 1

    (array[left], array[i-1]) = (array[i-1], array[left])
    return i-1


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

