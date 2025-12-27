class Solution:
    def checkPangram(self,s):
        English_Alphabet = "abcdefghijklmnopqrstuvwxyz"
        clean_list = [char.lower() for char in s if char.isalpha()]
        if len(set(clean_list)) != 26:
            return False
        return True
    