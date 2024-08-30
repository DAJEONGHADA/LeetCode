class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        answer = []

        for i in range(1, n):
            a = i
            b = n - a

            if '0' not in str(a) and '0' not in str(b):
                answer = [a, b]
        return answer