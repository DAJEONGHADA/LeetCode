class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # 각 divisor 별 divisibility score 저장
        d = {}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1
            d[divisor] = score
        max_score = max(d.values())

        answer = float('inf')
        for divisor, score in d.items():
            if score == max_score:
                if divisor < answer:
                    answer = divisor
        return answer