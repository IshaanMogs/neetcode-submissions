class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left=[0]*len(nums)
        right=[0]*len(nums)
        n=len(nums)-1
        answer=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                left[i]=1
            else:
                left[i]=left[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i==n:
                right[i]=1
            else:
                right[i]=right[i+1]*nums[i+1]
        for i in range(len(nums)):
            answer[i]=left[i]*right[i]
        return answer