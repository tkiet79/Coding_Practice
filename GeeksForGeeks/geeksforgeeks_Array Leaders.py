class Solution:
    def leaders(self, arr):
        new_arr = arr[::-1]
        res = [new_arr[0]]
        for i in range(1, len(new_arr)):
            if new_arr[i] >= res[-1]:
                res.append(new_arr[i])
        return res[::-1]

