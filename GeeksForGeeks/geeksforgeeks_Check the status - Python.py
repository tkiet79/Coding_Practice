class Solution:
    def checkStatus(self, a, b, flag):
        if a > 0 and b > 0:
            return False
        
        if a*b < 0 and flag == False:
            return True
        elif a*b > 0 and flag == True:
            return True
        
        return False