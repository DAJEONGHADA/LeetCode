class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n_str = str(n)
        answer = 0

        for i in range(len(n_str)):
            num = int(n_str[i])
            if i % 2 == 0:
                answer += num
            else:
                answer -= num
        return answer