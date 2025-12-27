class Solution:    
    def findUnion(self, a, b):
        return list(set.union(set(a),set(b)))