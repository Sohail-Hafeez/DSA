# The following code is correct but is brute force approach and its time complexity is O(n)

# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         output = []
#         j = 1
#         for i in range(len(nums)):
#             if j in nums:
#                 j=j+1
#                 continue
#             else:
#                 output.append(j)
#                 j=j+1
#         return output


# optimal code 
class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        
        # Step 1: Mark numbers as visited
        for num in nums:
            index = abs(num) - 1   # map number to index
            nums[index] = -abs(nums[index])
        
        # Step 2: Collect missing numbers
        output = []
        for i in range(n):
            if nums[i] > 0:
                output.append(i + 1)  # index i+1 is missing
                
        return output


        