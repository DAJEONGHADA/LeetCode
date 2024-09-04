class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        new_str_1 = s1[2] + s1[1] + s1[0] + s1[3]
        new_str_2 = s1[0] + s1[3] + s1[2] + s1[1]
        new_str_3 = s1[2] + s1[3] + s1[0] + s1[1]
        if s2 == s1 or s2 == new_str_1 or s2 == new_str_2 or s2 == new_str_3:
            return True
        else:        
            return False
    