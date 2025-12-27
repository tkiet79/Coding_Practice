class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = [haystack[k:len(needle)+k] for k in range(len(haystack)-(len(needle)-1))]
        if needle not in x:
            return -1
        return x.index(needle)