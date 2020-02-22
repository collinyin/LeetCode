# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

from typing import List

# NEWTON METHOD 
def mySqrt(x:int) -> int:
    root = x
    while root*root > x:
        previous = root
        root = (root + x/root)/2
        if (int(previous) == int(root)):
            break
        
    return int(root)

# CHEAT USING MATH LIBRARY
# import math
# def mySqrt(x:int) -> int:
#     return int(math.sqrt(x))

def main():
    print(mySqrt(100))

if __name__ == "__main__":
    main()