class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        # hint: while 문을 사용해서 n을 1로 만들 때까지
        # 2, 3, 5로 나눠주기
        # 만약 나눠지지 않는다면 False 리턴
        factors = [2, 3, 5]
        while True:
            if n == 1:
                break
            flag = False
            # 2, 3, 5로 나누어 떨어지는지 체크
            # 하나라도 나누어 떨어뜨리는 수가 없으면 return False
            # 나누어 떨어지면 해당 수로 n 나눠주기
            for factor in factors:
                if n % factor == 0:
                    flag = True
                    n /= factor
                    break
            if not flag:
                return False
        return True