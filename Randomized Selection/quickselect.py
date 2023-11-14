# https://github.com/sara-hrad
# The implementation of a randomized selection algorithm named as quickselect.
# This algorithm has the average running time of O(n).

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

# The main r_select function recursively find the kth smallest elements by comparing the
# index of pivot point in the partioned array and k.
def r_select(array, left, right, k):
    if 0 < k <= right - left + 1:
        partition_idx = partition(array, left, right)
        if partition_idx - left == k - 1:
            return array[partition_idx]
        elif partition_idx - left > k - 1:
            return r_select(array, left, partition_idx-1, k)
        else:
            return r_select(array, partition_idx + 1, right, k - partition_idx + left -1)


if __name__ == '__main__':
    array_example = [5, 6, 2300, 1, 0.5, 2]
    n_array = len(array_example)
    k = 2
    print(f"k-th smallest element of {array_example} is ", end="")
    print(r_select(array_example, 0, n_array - 1, k), end="")
    print(f' where k is {k}')
