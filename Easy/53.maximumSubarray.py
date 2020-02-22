# Given an integer array nums, find the contiguous subarray (containing at least one number) which 
# has the largest sum and return its sum.

from typing import List

# FIRST SOLUTION -- O(n^2)
# def maxSubArray(nums:List[int]) -> int:
        
#         if (len(nums) == 1):
#             return nums[0]
        
#         maxSum = nums[0]
#         maxPtr = 0
#         maxLength = 1
        
#         for i in range(len(nums)):
#             temp = 0
#             for j in range(i,len(nums)):
#                 temp += nums[j]
#                 if (temp > maxSum):
#                     maxSum = temp
#                     maxPtr = i
#                     maxLength = j-i+1
        
#         print("Starting from index:", str(maxPtr), "of length:", str(maxLength))
#         return maxSum

# nums = [1,2,3,1,2,3,2,4,5,-5,-23]
# print("Maximum sum subarray is:", maxSubArray(nums))


# IMPLEMENTING KADANE'S ALGORITHM
def maxSubArray(nums:List[int]) -> int:

    if (len(nums) == 1):
        return nums[0]

    # maxSum = nums[0]
    for i in range(1,len(nums)):
        if (nums[i-1] > nums[i] or nums[i-1] > 0):
            nums[i] += nums[i-1]
            # if (nums[i] > maxSum):
            #     maxSum = nums[i]
    return max(nums)
 
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))

if __name__ == "__main__":
    main()
