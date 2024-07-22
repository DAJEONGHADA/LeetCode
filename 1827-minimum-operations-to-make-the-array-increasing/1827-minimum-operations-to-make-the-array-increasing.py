class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 이전 숫자를 prev로 두고 현재 숫자와 비교
        prev = nums[0]
        answer = 0

        # 배열의 두 번째 요소부터 순차적으로 탐색
        for i in range(1, len(nums)):
            # 현재 숫자가 이전 숫자보다 작거나 같으면 연산 필요
            if nums[i] <= prev:
                # 필요한 연산 수를 계산
                calculate = prev - nums[i] + 1
                # 연산 횟수를 누적
                answer += calculate
                # 이전 숫자를 연산 후의 값으로 업데이트
                prev = prev + 1
            else:
                # 현재 숫자가 이전 숫자보다 크면 연산 필요 없음
                prev = nums[i]
        
        # 최종 연산 횟수를 반환
        return answer