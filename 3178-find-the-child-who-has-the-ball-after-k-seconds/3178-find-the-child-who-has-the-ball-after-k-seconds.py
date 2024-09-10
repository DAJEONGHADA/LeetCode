class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # modulo, children list 를 만든 다음, 뒤집어서 한번 붙이기
        children = [x for x in range(n)]
        queue = children + children[1:-1][::-1]
        # k가 queue 길이보다 작을 때는 그냥 k번째 element 리턴
        if k < len(queue):
            return queue[k]
        else:
            return queue[k % len(queue)]
        
        