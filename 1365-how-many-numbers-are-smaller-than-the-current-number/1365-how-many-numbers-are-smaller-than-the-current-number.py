class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = 0
        j=0
        output = []
        while j < len((nums)):
            for i in range(len(nums)):
                if( nums[j] > nums[i] ):
                    count +=1
            j = j+1
            output.append(count)
            count = 0
        return output

        