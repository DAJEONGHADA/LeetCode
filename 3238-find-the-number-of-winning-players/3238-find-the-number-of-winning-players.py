class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        answer = 0
        # key: 플레이어 번호, value: 각 색깔별 공 개수
        d = defaultdict(Counter)
        for player, ball_color in pick:
            d[player][ball_color] += 1
        for player, ball_counter in d.items():            
            max_balls = max(ball_counter.values())
            if max_balls > player:
                answer += 1
        return answer
