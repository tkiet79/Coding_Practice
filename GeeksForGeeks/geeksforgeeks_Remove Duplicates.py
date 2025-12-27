#User function Template for python3
class Solution:
	def removeDups(self, str):
		check_map = []
        for value in str:
            if value not in check_map:
                check_map.append(value)
            else:
                continue

        return ''.join(check_map)
		    