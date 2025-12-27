class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 1,2
        for i in range(3,n+1):
            current = a+b
            a = b
            b = current
        return b