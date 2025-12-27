s = "geEksforGEeks"  
class Solution:
    def reverse(self, s: str) -> str:
        stack = []
        res = []
        for value in s:
            stack.append(value)
        
        while len(stack) > 0:
            res.append(stack.pop())
        
        return ''.join(res)
