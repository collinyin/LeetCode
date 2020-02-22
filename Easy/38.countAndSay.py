# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11 (one 1)
# 3.     21 (two 1)
# 4.     1211 (one 2 one 1)
# 5.     111221 (one 1 one 2 two 1)

from typing import List

def countAndSay(self, n: int) -> str:
        
        if (n == 1):
            return "1"
        
        if (n == 2):
            return "11"
        
        sequence = ['1','1']
        
        while (n > 2):
            temp = []
            counter = 0
            ptr = 0
            
            for i in range(len(sequence)):
                if (sequence[i] == sequence[ptr]):
                    counter += 1
                else:
                    temp.append(str(counter))
                    temp.append(str(sequence[ptr]))
                    counter = 1
                    ptr = i
            
            temp.append(str(counter))
            temp.append(str(sequence[ptr]))
            sequence = temp
            n -= 1
        
        return ''.join(sequence)