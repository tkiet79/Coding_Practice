#User function Template for python3
class Solution:
    def DivisibleByEight(self,s):
        n = len(s)
        if n <= 3:
            num = int(s)
            if num%8 == 0:
                return 1
            else:
                return -1
        
        else:
            str1 = ""
            str1 = s[-3:]
            num1 = int(str1)
            if num1%8 == 0:
                return 1
            else:
                return -1