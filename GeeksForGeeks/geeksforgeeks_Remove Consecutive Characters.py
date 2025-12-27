#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, s):
        res = [s[0]]
        for value in s:
            if value != res[-1]:
                res.append(value)
       
        return ''.join(res)