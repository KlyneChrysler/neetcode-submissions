class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        count = {}

        for i, n in enumerate(nums):
            count[n] = count.get(n, 0) + 1

        res = sorted(count, key=count.get, reverse=True)

        return res[:k]
