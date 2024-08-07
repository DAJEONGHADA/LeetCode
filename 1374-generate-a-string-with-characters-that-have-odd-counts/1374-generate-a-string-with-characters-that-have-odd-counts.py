class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'p' * n
        else:
            return 'p' * (n - 1) + 'z' 