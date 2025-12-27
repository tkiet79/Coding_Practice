class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num # nếu 2 giá trị giống nhau ^ thì nó sẽ triệt tiêu còn nếu ^ với 0 thì sẽ ra chính nó
        return result 


    
     

    
