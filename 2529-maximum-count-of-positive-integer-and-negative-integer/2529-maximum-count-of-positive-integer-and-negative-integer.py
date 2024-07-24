class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        plus_answer = 0
        mi_answer = 0

        for num in nums:
            if num > 0:
                plus_answer += 1
            elif num < 0:
                mi_answer += 1

        return max(plus_answer, mi_answer)