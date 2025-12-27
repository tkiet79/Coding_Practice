class Solution:
    def intersectSize(self,a, b):
        a = set(a)
        b = set(b)
        res = a.intersection(b)
        return len(res)
