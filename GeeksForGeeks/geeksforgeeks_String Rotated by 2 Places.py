class Solution:
    def isRotated(self,s1,s2):
        if len(s1) != len(s2):
            return False
        
        n = len(s1)
        first_situation = ''.join([s1[2:n],s1[:2]])
        second_situation = ''.join([s1[n-2:n],s1[:n-2]])
        if s2 == first_situation or s2 == second_situation:
            return True
        return False
        