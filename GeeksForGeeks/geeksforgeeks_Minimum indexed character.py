class Solution:
    def minIndexChar(self,s1,s2): 
        n = len(s1)
        for i in range(n):
            if s1[i] in s2:
                return i
        
        return -1