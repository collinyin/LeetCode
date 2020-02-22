def quickSort(array):
    if len(array) <= 1:
        return array
    same = []
    left = []
    right = []
    pivot = array[0]
    for i in range(len(array)):
        if pivot > array[i]:
            left.append(array[i])
        elif pivot < array[i]:
            right.append(array[i])
        else:
            same.append(array[i])
    return quickSort(left) + same + quickSort(right)

def removeDups(array):
    return list(set(array))

a = [1,5,2,4,5,0,0,1,1,0,1,2,22222,2,22222222222222222222]
print(removeDups(quickSort(a))[1])
print(removeDups(quickSort(a))[-2])

