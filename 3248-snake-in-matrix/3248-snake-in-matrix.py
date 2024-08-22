class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # 위아래로 이동한 양, 좌우로 이동한 양 계산
        # 이를 그리드 상의 값으로 매핑
        c = Counter(commands)
        move_y = c['DOWN'] - c['UP']
        move_x = c['RIGHT'] - c['LEFT']
        return move_y*n + move_x