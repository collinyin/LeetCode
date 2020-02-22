# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, 
# and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

from typing import List

def plusOne(digits: List[int]) -> List[int]:
        
    string = ""
    for d in digits:
        string += str(d)
    return list(str(int(string) + 1))