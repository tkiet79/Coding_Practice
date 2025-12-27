class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                open_bracket = stack.pop() 
                if mapping[open_bracket] != char:
                    return False
        return not stack   