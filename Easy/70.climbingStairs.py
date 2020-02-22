# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

from typing import List
import time
# RECURSION SOLUTION
def climbStairs(n:int) -> int:
    # Base cases
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1
    elif (n == 2):
        return 2
    else:
        return climbStairs(n-2)+climbStairs(n-1)

# DYNAMIC PROGRAMMING SOLUTION
def dynamicClimbStairs(n:int) -> int:
    # Base cases
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    if (n == 2):
        return 2

    totalWays = 0
    oneBefore = 2
    twoBefore = 1
    i = 2
    while i < n:
        totalWays = oneBefore + twoBefore
        twoBefore = oneBefore
        oneBefore = totalWays
        i += 1
    return totalWays

def main():
    n = int(input())
    print("RECURSION SPEED")
    t = time.time()
    print(climbStairs(n))
    print(time.time() - t)
    print()
    print("DYNAMIC SPEED")
    t = time.time()
    print(dynamicClimbStairs(n))
    print(time.time() - t)
if __name__ == "__main__":
    main()

