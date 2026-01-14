class Solution(object):
    def findErrorNums(self, nums):
        a=nums
        nums.sort()
        j=1
        for i in nums:
            if i==nums[j]:
                duplicate = i
                break
            else:
                j = j+1
        k=1
        while(True):
            if k in a:
                k= k+1 
                continue
            else:
                replace = k
                break
        return [duplicate , replace]



        


        