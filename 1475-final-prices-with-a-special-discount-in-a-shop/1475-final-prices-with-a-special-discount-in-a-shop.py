class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 2중 for문 사용
        answer = []
        for i in range(len(prices)):
            flag = False
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    # discount 된 금액을 계산해서 answer에 추가
                    answer.append(prices[i] - prices[j]) 
                    flag = True
                    break
            # flag 값이 True가 아니면 answer에 현재 가격 그대로 추가
            if not flag:
                answer.append(prices[i])
        return answer
