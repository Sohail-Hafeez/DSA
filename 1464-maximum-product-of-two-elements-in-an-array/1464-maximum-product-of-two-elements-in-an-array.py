class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = 0
        Max = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:     
                    answer = (nums[i]-1) * (nums[j]-1) 
                    Max = max(answer , Max)
        return max(answer , Max)