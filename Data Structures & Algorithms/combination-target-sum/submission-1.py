class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #for each elem in the thing
        #run array builder on it
        #basically makes a blank array and just tries to build up a valid thing and if equals 9 then append to res, if exceeds 9 then moves on. oh fuck tho it can eb unlimited number of times. So actually we're gonna do like a fucking decision tree .
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            #decisions!
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            #other one
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
