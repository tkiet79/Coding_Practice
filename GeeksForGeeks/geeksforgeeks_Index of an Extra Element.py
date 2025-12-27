class Solution:
    def findExtra(self,a,b):
        for i in range(len(b)):
            if a[i] != b[i]:
                return a.index(a[i])
        return len(b) 