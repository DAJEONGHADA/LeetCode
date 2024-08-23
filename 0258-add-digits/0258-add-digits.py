class Solution:
    def addDigits(self, num: int) -> int:
        # while문, 숫자 -> 문자열 -> 숫자
        while num >= 10:
            # 각 자릿 수의 합계를 num에다가 입력
            digit_sum = 0
            for c in str(num):
                digit_sum += int(c)
            num = digit_sum
        return num
    
