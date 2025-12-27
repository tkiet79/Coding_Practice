#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        total = 0
        for value in str(n):
            total += int(value)**3
        
        return total == n
            