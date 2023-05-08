def merge_sort_ascending(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort_ascending(left)
        merge_sort_ascending(right)

        i = 0
        j = 0
        k = 0

        while i < len(right) and j < len(left):
            if right[i] < left[j]:
                data[k] = right[i]
                i += 1
            else:
                data[k] = left[j]
                j += 1
            k += 1

        while i < len(right):
            data[k] = right[i]
            i += 1
            k += 1

        while j < len(left):
            data[k] = left[j]
            j += 1
            k += 1

    return data

lst1 = [1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,1,2000,3,56]
lst2 = [20,21,22,23,24,25,26,27]
lst3 = [30,29,31,33,19,20,31,21,59]

print(merge_sort_ascending(lst1))
print(merge_sort_ascending(lst2))
print(merge_sort_ascending(lst3))
