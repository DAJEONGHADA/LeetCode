class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        answer = 0
        n = len(hours)

        # Iterate through all possible pairs (i, j) with i < j
        for i in range(n):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    answer += 1

        return answer