class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Dictionary as we can leverage O(1) num:index lookup 
        elements = {}
        for index, num in enumerate(nums): # need some way to also keep index ig enumerate
            search = target - num
            if search in elements:
                return [elements[search], index]
            else:
                elements[num] = index
        return []
        #so for each number we first will calculate the (target - num) to find whatever other number we're looking for. 
        #then check if it's in the dictionary, if so we return the index plus current index
            #else add current num and index to dict
        