class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # sorting, pop
        # pop(0), pop()
        # while
        nums = sorted(nums)
        # print(nums)
        averages = []
        while nums:
            min_num = nums.pop(0)
            max_num = nums.pop()
            # print(min_num ,max_num)
            # min_num, max_num의 평균값을 averages에 추가할 것
            averages.append((min_num + max_num) / 2)
        # averages의 min 값을 리턴할 것
        return min(averages)