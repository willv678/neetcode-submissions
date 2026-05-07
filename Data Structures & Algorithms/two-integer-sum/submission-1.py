class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #ok here we just make a dictionary thats like key value of num:index or whichever one has the instant loookups assumably num:index is proper here
        #then for loop thru it,
            #calc needed num just target - num
            #if that needed is in dict the nreturn current index maybe enum instead ig + dict's value for that key
        seenNumbers = {}
        for index, num in enumerate(nums):
            goal = target - num
            if goal in seenNumbers:
                return [seenNumbers[goal], index]
            else:
                seenNumbers[num] = index