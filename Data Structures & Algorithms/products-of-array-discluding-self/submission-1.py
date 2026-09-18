class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suff= [1] *len(nums)
        preff = [1] * len(nums)
        result=[1] *len(nums)
        for i in range(1,len(nums)):
            preff[i]=preff[i-1]*nums[i-1]

        for j in range(len(nums)-2,-1,-1):
            suff[j]=suff[j+1]*nums[j+1]

        for i in range(len(nums)):
            result[i]=suff[i]*preff[i]  
        return result          