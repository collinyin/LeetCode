# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

from typing import List

def removeDuplicates(nums:List[int]) -> int:

    # MY SOLUTION (O(n^2))
        # ptr1 = 0
        # ptr2 = 0
        # if (len(nums) > 1):
        #     ptr2 = 1
        # else:
        #     return len(nums)

        # while True:
        #     if (len(nums) > 1):
        #         if (nums[ptr1] == nums[ptr2]):
        #             nums.pop(ptr1)
        #             ptr1 = 0
        #             ptr2 = 0
        #         if (ptr2 == len(nums)-1):
        #             ptr1 += 1
        #             ptr2 = ptr1
        #             if (ptr1 == len(nums)-1):
        #                 break
        #         ptr2 += 1
        #     else:
        #         break
        #     # print(nums)
        # return len(nums)

    # ONLINE SOLUTION (O(n)) - understood!
        if (len(nums) < 1):
            return 0
        
        ptr = 0

        for i in range(1,len(nums)):
            if (nums[i] != nums[ptr]):
                ptr += 1
                nums[ptr] = nums[i]
        
        # print(nums)
        return ptr + 1

nums = [-50,-50,-49,-48,-48,-48,-47,-47,-47,-47,-46,-45,-43,-42,-42,-42,-42,-42,-42,-41,-41,-39,-38,-38,-37,-37,-36,-36,-34,-33,-33,-33,-32,-32,-31,-31,-31,-30,-30,-29,-29,-28,-28,-28,-26,-26,-26,-26,-25,-25,-25,-25,-24,-24,-24,-23,-22,-21,-21,-20,-20,-20,-19,-18,-18,-17,-17,-16,-16,-16,-16,-15,-14,-14,-13,-13,-13,-13,-13,-12,-12,-11,-10,-10,-9,-9,-9,-8,-8,-8,-7,-6,-5,-5,-5,-4,-4,-3,-3,-2,-2,-2,-2,-1,0,0,2,2,2,3,3,3,4,5,5,5,6,6,6,8,8,10,10,11,12,12,13,13,14,14,14,15,15,16,16,17,17,17,18,18,20,20,20,21,21,21,21,22,22,25,25,25,26,26,27,28,28,29,29,29,29,30,30,30,33,33,33,34,35,35,35,36,38,38,38,39,39,40,41,41,41,41,42,42,42,43,44,44,45,45,46,48,48,50,50,50]
print(removeDuplicates(nums))