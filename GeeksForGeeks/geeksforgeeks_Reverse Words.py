class Solution:
    def reverseWords(self, s):
        s = s.split('.')
        s = [val for val in s if val != '']
        s = '.'.join(s[::-1])
        return s
        