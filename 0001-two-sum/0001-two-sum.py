class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for i, num in enumerate(nums):
            calculate = target - num
            if calculate in d:
                return [i, d[calculate]]
            else:
                d[num] = i