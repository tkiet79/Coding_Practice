class Solution:
    def deleteMid(self, stack):
        stack.pop(((len(stack) + 1)//2) - 1)
        return stack[::-1]
        
