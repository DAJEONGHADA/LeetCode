class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # 숫자를 문자열로 변환, 각 자릿수의 합계 구해보기
        answer = 0
        for i in str(x):
            answer += int(i)
    
        if x % answer == 0:
            return answer
        else:
            return -1