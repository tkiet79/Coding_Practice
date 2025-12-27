class Solution:
    def isBalanced(self, s):
        stack = []
        check = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for char in s:
            if char in check:
                if not stack:
                    return False
            
                if stack.pop() != check[char]:
                    return False
            
            else:
                stack.append(char)
        
        return len(stack) == 0



                




        








