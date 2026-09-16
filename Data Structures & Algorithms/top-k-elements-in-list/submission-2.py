from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a dict, go thru and incremeent the value as u see it then just sort and return the top k ? cna u do that ?
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        sorted_keys = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

        return sorted_keys[:k]
