class Solution:
    def firstRepChar(self, s):
        strs_map = dict.fromkeys(s,0)
        for value in s:
            strs_map[value] += 1
            if strs_map[value] == 2:
                return value
        
        return -1