# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

from typing import List

# ONE LINE SOLUTION.
# def addBinary(a: str, b: str) -> str:
#     return bin(eval('0b' + a) + eval('0b' + b))[2:]

# UGLIEST CODE I'VE WRITTEN IN A WHILE LOL... BUT IT WORKS, WHATEVER.
def addBinary(a: str, b: str) -> str:
    
    output = []
    carry = False
    length = len(a)
    diff = len(b)-len(a)
    
    if (len(a) >= len(b)):
        diff = len(a)-len(b)
        length = len(b)
    
        for i in range(length-1,-1,-1):
            if (carry == True):
                if (a[i+diff] == '1' and b[i] == '1'):
                    output.insert(0,'1')
                    carry = True
                elif (a[i+diff] == '0' and b[i] == '0'):
                    output.insert(0,'1')
                    carry = False
                else:
                    output.insert(0,'0')
                    carry = True
            else:
                if (a[i+diff] == '1' and b[i] == '1'):
                    output.insert(0,'0')
                    carry = True
                elif (a[i+diff] == '0' and b[i] == '0'):
                    output.insert(0,'0')
                    carry = False
                else:
                    output.insert(0,'1')
                    carry = False
    else:
        for i in range(length-1,-1,-1):
            if (carry == True):
                if (a[i] == '1' and b[i+diff] == '1'):
                    output.insert(0,'1')
                    carry = True
                elif (a[i] == '0' and b[i+diff] == '0'):
                    output.insert(0,'1')
                    carry = False
                else:
                    output.insert(0,'0')
                    carry = True
            else:
                if (a[i] == '1' and b[i+diff] == '1'):
                    output.insert(0,'0')
                    carry = True
                elif (a[i] == '0' and b[i+diff] == '0'):
                    output.insert(0,'0')
                    carry = False
                else:
                    output.insert(0,'1')
                    carry = False

    if (len(a) > len(b)):
        
        for i in range(len(a)-len(b)-1,-1,-1):
            if (carry == True):
                if (a[i] == '1'):
                    output.insert(0,'0')
                    carry = True
                else:
                    output.insert(0,'1')
                    carry = False
            else:
                if (a[i] == '1'):
                    output.insert(0,'1')
                else:
                    output.insert(0,'0')
                    
    elif (len(b) > len(a)):
        for i in range(len(b)-len(a)-1,-1,-1):
            if (carry == True):
                if (b[i] == '1'):
                    output.insert(0,'0')
                    carry = True
                else:
                    output.insert(0,'1')
                    carry = False
            else:
                if (b[i] == '1'):
                    output.insert(0,'1')
                else:
                    output.insert(0,'0')
    
    if (carry == True):
        output.insert(0,'1')
        carry = False
    
    binarySum = ""
    for i in range(len(output)):
        binarySum += output[i]
    
    return binarySum

def main():
    str1 = "1110010000001111101010100001"
    str2 = "11100100001000101010010101010101001"
    print(str1, "+", str2, "=", addBinary(str1,str2))

if __name__ == "__main__":
    main()
