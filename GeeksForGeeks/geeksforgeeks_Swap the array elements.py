class Solution:
	def swapElements(self, arr):
	    left = 0
	    right = 2
	    n = len(arr)
	    if n < 3:
	        return arr
	        
	    while right < n:
	        arr[left], arr[right] = arr[right], arr[left]
	        left += 1
	        right += 1
	   
	    return arr
	        