class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # 2 hàm nếu length khác nhau thì chắc chắn ko phải anagram
            return False 
        
        
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0)+1 # count[s[i]] nếu có thì lấy giá trị +1, ko có thì gán =0 +1
            countT[t[i]] = countT.get(t[i],0)+1 # tương tự với t[i]
        
        return countS == countT # không quan trọng thứ tự, chỉ so các cặp key:value có giống nhau ko