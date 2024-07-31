class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # for, sorted, pop(가장 마지막에 있는 리스트를 빼준다)
        for i in range(k):
            # 리스트를 정렬하여 가장 큰 값을 추출
            gifts.sort()
            max_gifts = gifts.pop()
            
            # 가장 큰 값의 제곱근을 계산하여 다시 gifts 리스트에 추가
            sqrt_max_gifts = int(math.sqrt(max_gifts))
            gifts.append(sqrt_max_gifts)
        
        # 최종적으로 gifts 리스트의 합을 반환
        return sum(gifts)