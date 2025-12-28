#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        n = 32
        bin_x = bin(x)[2:]
        n_x = len(bin_x)
        
        num = '0' * (n - n_x) + bin_x
        res = num[::-1]
        
        return int(res, 2)
        