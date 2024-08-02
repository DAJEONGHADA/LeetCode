class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
#         sort_nums = sorted(nums)

#         answer = []
#         for i in range(len(sort_nums)):
#             if sort_nums[i] == target:
#                 answer.append(i)

#         return answer
    
        return [i for i, num in enumerate(sorted(nums)) if num == target]