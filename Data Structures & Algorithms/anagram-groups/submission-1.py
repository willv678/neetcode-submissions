class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0]*26 #a thru z
            for c in s: #now for each word
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return list(result.values())

        #Yeah this one is weird. I think the defaultdict is new, 
        #the ord(c) - ord("a") is also quite new.