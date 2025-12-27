class Solution:
    def sumOfDivisors(self, n):
        ans = 0
        for i in range(1,n+1):
            ans += int((i*(n//i)))
        
        return ans