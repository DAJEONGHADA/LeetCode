class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # 초기값을 True로 설정
        answer = True
        # for문을 사용하여 현재 위치와 다음 위치의 숫자의 홀짝 비교
        for i in range(len(nums) - 1):
            # 현재 숫자와 다음 숫자의 홀짝이 같다면 특별 배열 조건 위배
            if (nums[i] % 2) == (nums[i + 1] % 2):
                answer = False
                break
        
        return answer