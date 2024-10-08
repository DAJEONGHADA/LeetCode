class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        answer = 0
        prev = 0
        for upper, percent in brackets:
            if upper <= income:
                # 세금을 내야할 양 계산하고, 세율을 곱해서 answer에 더해주기
                amount = upper - prev
                answer += amount * (percent / 100)
                prev = upper
            else:
                # 세금을 내야할 양 계산하고, 세율을 곱해서 answer에 더해주기
                amount = income - prev
                answer += amount * (percent / 100)
                break
        return answer