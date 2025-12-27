class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''.join(list(map(str,digits)))
        nums = int(num_str) + 1
        output_value = list(map(int,[value for value in str(nums)]))
        return output_value