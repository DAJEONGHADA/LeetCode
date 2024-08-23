class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  # num이 한 자릿수가 될 때까지 반복
            sum = 0
            while num > 0:
                sum += num % 10  # num의 마지막 자릿수를 더함
                num //= 10  # 마지막 자릿수를 제거
            num = sum  # sum을 num으로 갱신

        return num