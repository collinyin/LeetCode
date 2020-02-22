# Implementing quick sort (No space constraint)

from typing import List

def quickSort(nums:List[int]) -> List[int]:

    if (len(nums) <= 1):
        return nums
    
    pivot = nums[0]
    less = []
    equal = []
    greater = []

    for n in nums:
        if (n < pivot):
            less.append(n)
        elif (n == pivot):
            equal.append(n)
        else:
            greater.append(n)
    
    return quickSort(less) + equal + quickSort(greater)


def main():
    nums = [1,2,5,3,2,5,2,3,1,6]
    print(quickSort(nums))

if __name__ == "__main__":
    main()