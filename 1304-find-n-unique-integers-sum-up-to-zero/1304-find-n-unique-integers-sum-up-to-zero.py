class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        for i in range(1, n // 2 + 1):
            answer.append(i)    # 양수 추가
            answer.append(-i)   # 음수 추가
            
        if n % 2 != 0:  # n이 홀수면 0 추가
            answer.append(0)

        return answer