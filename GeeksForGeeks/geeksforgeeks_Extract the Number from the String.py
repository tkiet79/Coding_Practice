class Solution:
    def ExtractNumber(self,sentence):
        arr = sentence.split()
        res = []
        
        for value in arr:
            if value.isdigit():
                res.append(int(value))
        
        res = list(map(str, sorted(res, reverse=True)))
        for val in res:
            if '9' not in val:
                return val
        
        return -1
        
        
            