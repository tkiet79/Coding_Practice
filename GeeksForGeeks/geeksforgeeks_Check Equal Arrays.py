class Solution:
    def checkEqual(self, a, b) -> bool:
        check_a = dict.fromkeys(a,0)
        check_b = dict.fromkeys(b,0)
        for value in a:
            check_a[value] += 1
            
        for value in b:
            check_b[value] += 1
            
        return check_a == check_b

