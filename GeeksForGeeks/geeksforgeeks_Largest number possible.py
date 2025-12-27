#User function Template for python3

class Solution:
    def findLargest(self, n, s):
        if s == 0 and n > 1 or s > 9 * n:
            return -1
        res = []
        for i in range(n):
            digit = min(9,s)
            res.append(str(digit))
            s = s-digit
        ans = ''.join(res)
        return ans
        
    