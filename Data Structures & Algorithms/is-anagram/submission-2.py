class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = [0] * 26
        tCount = [0] * 26
        #okobv len check its false if not equal
        #make 2 arrays ig like sArray and tArray both 26 0s.
        for char in s:
            sCount[(ord(char) - ord('a'))] += 1
        for char in t:
            tCount[(ord(char) - ord('a'))] += 1
        if sCount == tCount:
            return True
        return False