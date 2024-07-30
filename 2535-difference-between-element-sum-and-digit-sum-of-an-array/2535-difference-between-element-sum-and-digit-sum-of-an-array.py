class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # for문으로 반복
        # num을 문자열로 만들고, 다시 for문을 돌면 각 자릿수를 가져올 수 있음
        # element_sum = sum(nums)
        nums_sum = sum(nums)
        
        # 자릿수 합 계산
        answer = 0
        for num in nums:
            for c in str(num):
                answer += int(c)
        
        # 절대 차이 계산
        return abs(nums_sum - answer)