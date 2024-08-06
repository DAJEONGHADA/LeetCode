class Solution:
    def isPowerOfThree(self, n: int) -> bool:
#         # while문 사용
#         if n <= 0:
#             return False
#         while n % 3 == 0:
#             n //= 3        # n //= 3는 n을 3으로 나눈 몫으로 갱신, n이 3의 거듭제곱인지 확인하기
#         return n == 1      # 1이라면 n은 3의 거듭제곱이므로 True를 반환하고, 그렇지 않으면 False를 반환


        if n <= 0:
            return False
        while True:
            if n == 1:
                break
            if n % 3 != 0:
                return False
            n //= 3
        return True
    