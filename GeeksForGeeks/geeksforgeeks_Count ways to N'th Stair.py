#User function Template for python3


class Solution:

    #Function to count number of ways to reach the nth stair
    #when order does not matter.
    def countWays(self, n):
        mod = 1000000007
        
        count = 1
        return count + n//2