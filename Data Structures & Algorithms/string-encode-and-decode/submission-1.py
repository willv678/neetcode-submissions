class Solution:

    def encode(self, strs: List[str]) -> str:
        #hello world = 5#hello5#world
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)
        #literally just append that to it like wc # word 

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Locate delimiter
            j = s.find('#', i)     # ok 5#hello so j is # . so the start is the first cvhar h and end is h + 
            length = int(s[i:j])
            
            # Slice word
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Advance pointer past current string
            i = end
            
        return res