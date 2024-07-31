class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # 2중 for문, list slice
        answer = float('inf')
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                part_one = nums[:i]
                part_two = nums[i:j]
                part_three = nums[j:]

                current_cost = part_one[0] + part_two[0] + part_three[0]
                answer = min(answer, current_cost)
                # answer와 비교해서 더 작은 값을 answer로 지정
        return answer
