class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        answer = 0
        
        str_1 = str(num1).zfill(4)
        str_2 = str(num2).zfill(4)
        str_3 = str(num3).zfill(4)
        
        for i, j, k in zip(str_1, str_2, str_3):
            min_digit = min(i, j, k)
            answer = answer * 10 + int(min_digit)
        
        return answer
