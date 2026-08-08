class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for i in range(len(nums)*2):
            if i>len(nums)-1:
                i=i%len(nums)
            ans.append(nums[i])
        return ans
        