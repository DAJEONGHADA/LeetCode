class Solution:
    def arraySign(self, nums: List[int]) -> int:
        answer = 1
        for num in nums:
            if num == 0:
                answer *= 0
                break
            elif num < 0:
                answer *= -1
        return answer
    