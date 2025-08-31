from collections import deque

class Solution(object):
    def addBinary(self, a):
        q = deque()
        carry = 1   # we want to add 1

        # iterate from last bit to first
        for i in range(len(a) - 1, -1, -1):
            bit = int(a[i]) + carry
            if bit == 2:
                q.appendleft('0')
                carry = 1
            else:
                q.appendleft(str(bit))
                carry = 0

        # if carry is still left (overflow case, e.g. 111 + 1 = 1000)
        if carry == 1:
            q.appendleft('1')

        # count ones
        ones = sum(1 for b in q if b == '1')

        return "".join(q), ones


    def countBits(self, n):
        res = [0]        # ans[0] = 0
        nextNum = "0"    # binary for 0
        for _ in range(n):    # run n times
            nextNum, ones = self.addBinary(nextNum)
            res.append(ones)
        return res
