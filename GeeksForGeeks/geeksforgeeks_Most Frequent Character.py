class Solution:
    def getMaxOccurringChar(self, s):
        check = dict.fromkeys(s, 0)
        for value in s:
            check[value] += 1
      
        check = dict(sorted(check.items()))
        for char, count in check.items():
            if count == max(check.values()):
                return char
            
        