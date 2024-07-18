class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        # 4중 for 문
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for p in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] == nums[p]:
                            answer += 1
        return answer