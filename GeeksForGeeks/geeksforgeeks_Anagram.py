class Solution:
    def areAnagrams(self, s1, s2):
        check_s1 = dict.fromkeys(s1, 0)
        check_s2 = dict.fromkeys(s2,0)
        for value in s1:
            check_s1[value] +=1

        for value in s2:
            check_s2[value] +=1

        return check_s1 == check_s2