class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        answer = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] == diff:
                    for k in range(j + 1, n):
                        if nums[k] - nums[j] == diff:
                            answer += 1

        return answer