class Solution(object):
    def findErrorNums(self, nums):
        if nums == [1,1]:
            return [1,2]
        j = 1
        check = 0
        c = False
        for i in nums:
            if (i != nums[j]):
                j = j+1
                c = True
                continue
            else:
                check=i
                break
        if c == False:
            j = j+1
        if (check + 1) in nums and check - 1 in nums:
            return -1
        if (check-1) in nums:
            return [j, check + 1]
        else:
            return [j , check - 1]
        


        