class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        majority_element = dict.fromkeys(arr,0)

        for value in arr:
            majority_element[value] += 1

        for num, count in majority_element.items():
            if count > n//2:
                return num
        else:
            return -1