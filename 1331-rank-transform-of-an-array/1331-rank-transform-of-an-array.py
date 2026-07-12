class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_unique = sorted(list(set(arr)))
        ranks = {num: rank for rank, num in enumerate(sorted_unique, 1)}
        return [ranks[num] for num in arr]