class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create the dict
        seen = {}
        #for num in nums but enum r wtv so u hasve counter too
        for i, num in enumerate(nums):
            #calculate goal = sum - num
            goal = target - num
            #if goal in nums
            if goal in seen:
            #return current enum and dict's index value
                return [seen[goal], i]
            #else add this num and index to dict
            seen[num] = i
