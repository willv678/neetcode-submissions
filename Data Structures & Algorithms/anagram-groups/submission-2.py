from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
            #so go throhg and put the sorted in dictionary def ? Like ig i sort it and be like sor = s.sorted() r wtv and then add the unsorted to that sorted's key ? then at teh end we just print it all ? 