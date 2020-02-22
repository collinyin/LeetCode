# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

from typing import List

class Solution:
    # MY BETTER SOLUTION :)
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        prevList = self.getRow(rowIndex-1)
        row = [1]
        for i in range(1, len(prevList)):
            newVal = prevList[i-1] + prevList[i]
            row.append(newVal)
        row.append(1)
        
        return row
    
    def generate(self, numRows: int) -> List[List[int]]:
        finalList = []
        for i in range(numRows):
            finalList.append(self.getRow(i))
        return finalList

    # ONLINE FAST SOLUTION (MUCH BETTER....)
    # def generate(self, numRows: int) -> List[List[int]]:
    #     finalList = []
    #     for i in range(numRows):
    #         finalList.append([1] * (i + 1))
    #         if i > 1:
    #             for j in range(1, i):
    #                 finalList[i][j] = finalList[i-1][j-1] + finalList[i-1][j]
    #     return finalList

    # MY HORRIBLE RECURSIVE SOLUTION...
    # def getRow(self, numRows: int, finalList) -> List[int]:
    #     if numRows == 1:
    #         finalList.append([1])
    #         return [1]
    #     if numRows == 2:
    #         finalList.append([1,1])
    #         return [1,1]
        
    #     tempList = [1]
    #     for i in range(1,numRows-1):
    #         temp = self.getRow(numRows-1, finalList)
    #         tempList.append(temp[i]+temp[i-1])
    #     tempList.append(1)

    #     finalList.append(tempList)
    #     return tempList
    
    # def removeDups(self, duplicate: List[List[int]]):
    #     final_list = [] 
    #     for num in duplicate: 
    #         if num not in final_list: 
    #             final_list.append(num) 
    #     return final_list
                    
    
    # def generate(self, numRows: int) -> List[List[int]]:
    #     finalList = []
    #     for i in range(1, numRows + 1):
    #         self.getRow(i, finalList)
        
    #     return self.removeDups(finalList)


def main():
    sol = Solution()
    print(sol.generate(10))

if __name__ == "__main__":
    main()
