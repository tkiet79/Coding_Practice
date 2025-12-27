class Solution:
    def findTwoElement(self, arr):
        n = len(arr) + 1
        res = []
        check_dup = dict.fromkeys(arr,0)
        for value in arr:
            check_dup[value] += 1
        for num,count in check_dup.items():
            if count == 2:
                res.append(num)

        arr.sort()
        missing_num = sum(i for i in range(1,n)) - sum(arr) + res[0]
        res.append(missing_num)
        
        return res