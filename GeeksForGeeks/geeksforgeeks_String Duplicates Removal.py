s = "geEksforGEeks"  # geEksforG
#User function Template for python3
class Solution:

	def removeDuplicates(self, s):
	    l = []
        for value in s:
            if value not in l:
                l.append(value)
    
            else:
                continue

        return ''.join(l)
