class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            calculate = num % 3
            if calculate == 1:
                answer += 1
            elif calculate == 2:
                answer += 1
        return answer