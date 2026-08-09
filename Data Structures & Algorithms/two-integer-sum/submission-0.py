class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            d[nums[i]]= i
        for i in range(len(nums)):
            req = target-nums[i]
            if req in d and d[req]!=i:
                return [i,d[req]]