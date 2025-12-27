class Solution:
    # cách làm bằng AI 
    ''' O(m + n) '''
    def rowWithMax1s(self, arr):
        if not arr or not arr[0]:
            return -1
        R = len(arr)
        C = len(arr[0])
        row = 0
        col = C - 1
        res = -1
        while row < R and col >= 0:
            if arr[row][col] == 1:
                res = row
                col -= 1
            else:
                row += 1    
        return res
    
    # cách ban đầu
    ''' O(m x n) '''
    def rowWithMax1s(self, arr):
        max_value = 0
        res = -1
        for i in range(len(arr)):
            if arr[i][0] == 1:
                return i
            if sum(arr[i]) > max_value:
                max_value = sum(arr[i])
                res = i
        
        return res