# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
# return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

from typing import List

def lengthOfLastWord(s:str) -> int:

    try:
        strList = s.split()     #.split() with arguments splits according to white spaces :)
        # print(strList)
        return int(len(strList[-1]))
    except:
        return 0

def main():
    s = "b   a    "
    print(lengthOfLastWord(s))

if __name__ == "__main__":
    main()