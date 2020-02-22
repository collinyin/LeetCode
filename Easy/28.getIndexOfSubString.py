# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

from typing import List

def strStr(self, haystack: str, needle: str) -> int:
    
    if (len(needle) < 1):
        return 0
    
    for i in range(len(haystack)):
        sliceObj = slice(i,len(needle)+i,1)
        if (haystack[sliceObj] == needle):
            return i
    
    return -1
    