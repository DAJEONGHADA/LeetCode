class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        # for, enumerate
        answer = -1
        for i, num in enumerate(nums):
            if i % 10 == nums[i]:
                return i
        return answer