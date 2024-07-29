class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit = []
        double_digit = []
        # 1. 한자리 수만 모아서 single_digit에 추가하기
        # 2. 두자리 수만 모아서 double_digit에 추가하기
        # 전체 합계에서 single_digits 합계를 빼준 값과 비교
        # 전체 합계에서 double_digits 합계를 빼준 값과 비교
        single_digit = []
        double_digit = []

        # 1. 한 자리 숫자와 두 자리 숫자를 각각의 리스트에 추가하기
        for num in nums:
            if num < 10:
                single_digit.append(num)
            elif num < 100:
                double_digit.append(num)
        
        # 전체 합계 구하기
        total_sum = sum(nums)
        # single_digit 합계 구하기
        single_sum = sum(single_digit)
        # double_digit 합계 구하기
        double_sum = sum(double_digit)
        
        # Alice가 이길 수 있는지 확인하기
        if single_sum > (total_sum - single_sum) or double_sum > (total_sum - double_sum):
            return True
        else:
            return False
