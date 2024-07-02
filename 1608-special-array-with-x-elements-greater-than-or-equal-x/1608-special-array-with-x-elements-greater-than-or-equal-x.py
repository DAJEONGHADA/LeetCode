class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        answer = -1
        
#         i번째 elenet가 x 보다 같거나 크고
#         i+1 번째 element가 x보다 작으면 special!
#         이때, i+1 번째 element가 존재하지 않는 경우 예외 처리

#         [4, 4, 3, 0, 0]
#          0, 1, 2, 3, 4, 5
#          만약 0일 때 special 이라면 0보다 큰 수가 0개 이여야 한다.  X
#          만약 1일 때 special 이라면 1보다 같거나 큰 수가 1개 있어야 한다. X
#          만약 2일 때 special 이라면 2보다 같거나 큰 수가 2개 있어야 한다. X
#          만약 3일 때 special 이라면 3보다 같거나 큰 수가 3개 있어야 한다. 0
        for i in range(len(nums)):
            x = i + 1
            if i == len(nums) - 1:
                if nums[i] >= x:
                    answer = x
            elif nums[i] >= x and nums[i+1] < x:
                answer = x
                break
        return answer