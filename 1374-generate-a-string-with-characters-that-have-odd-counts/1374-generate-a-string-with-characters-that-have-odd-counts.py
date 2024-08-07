class Solution:
    def generateTheString(self, n: int) -> str:
        answer = ""
        if n % 2 == 1:
            answer = 'p' * n
        else:
            answer = 'p' * (n - 1) + 'z'
            
        return answer