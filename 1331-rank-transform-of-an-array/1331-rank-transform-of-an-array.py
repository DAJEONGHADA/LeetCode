class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # set, dict
        rank_dict = {x: (i + 1) for i, x in enumerate(sorted(set(arr)))}
        return [rank_dict[x] for x in arr]