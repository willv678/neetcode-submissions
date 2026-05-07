class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge cases
        if len(s) != len(t):
            return False
        #initialize frequency maps for each word
        dictS = {}
        dictT = {}
        for letter in s:
            #add it to dict / incremeent it by one
            dictS[letter] = dictS.get(letter, 0) + 1
        for letter in t:
            #add it to dict / increment it by one
            dictT[letter] = dictT.get(letter, 0) + 1
        #Both frequency maps created, now compare
        for letter in dictS:
            if dictS != dictT:
                return False
        return True