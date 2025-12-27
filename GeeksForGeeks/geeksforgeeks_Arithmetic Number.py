#User function Template for python3

class Solution:
    def inSequence(self, a, b, c):
        n = ((b - a) / c) + 1
        return n == int(n)