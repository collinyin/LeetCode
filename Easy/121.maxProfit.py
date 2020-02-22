# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell 
# one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

from typing import List

class Solution:
    def quickSort(self, array: List[int]) -> List[int]:
        # base case
        if len(array) <= 1:
            return array
        
        same = []
        left = []
        right = []
        pivot = array[0]
        
        for a in array:
            if a < pivot:
                left.append(a)
            elif a > pivot:
                right.append(a)
            else:
                same.append(a)

        return self.quickSort(left) + same + self.quickSort(right)
        
    def reverse(self, array: List[int]) -> List[int]:
        rList = []
        for i in range(len(array)-1,-1,-1):
            rList.append(array[i])      
        
        return rList      

    def maxProfit(self, prices: List[int]) -> int:
#         NAIVE SOLUTION (O(n^2))

#         optimalDifference = 0
#         for i in range(len(prices)-1):
#             for j in range(i, len(prices)):
#                 currDifference = prices[j]-prices[i]
#                 if currDifference > optimalDifference:
#                     optimalDifference = currDifference
        
#         return optimalDifference

# My new solution:
# have a reversed sorted list of the values then compare the largest pairs
# then look at the index of the pair, if the index is positive then return the difference
        
        sortedList = self.reverse(self.quickSort(prices))
        print(sortedList)
        priceDict = {}
        for i in range(len(prices)):
            priceDict.update({prices[i] : i})
        print(priceDict)

        maxDiff = 0
        # for i in range(int(len(sortedList)/2)):
        #     if key(sortedList[i]) > key(sortedList[len(sortedList)-1-i]):
        #         maxDiff = sortedList[i] - sortedList[len(sortedList)-1-i]
        
        return maxDiff
            
def main():
    a = [1,4,2,3,5,2,4,6,74,1,0]
    sol = Solution()
    sol.maxProfit(a)

if __name__ == "__main__":
    main()
