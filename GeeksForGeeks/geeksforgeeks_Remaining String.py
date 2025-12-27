#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
	    n = len(s)
	    for i in range(n):
	        if s[i] == ch:
	            count -= 1
            
            if count == 0 and i != n-1:
                return s[i+1:n]
        
        return ''
	       
	        
		    