class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # 2중 for 문
        
        answer = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(1+i, n):
                if abs(nums[i] - nums[j]) == k:
                    answer +=1
        return answer