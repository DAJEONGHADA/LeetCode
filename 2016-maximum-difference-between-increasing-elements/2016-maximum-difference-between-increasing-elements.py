class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    max_diff = nums[j] - nums[i]
                    answer = max(answer, max_diff)
        return answer