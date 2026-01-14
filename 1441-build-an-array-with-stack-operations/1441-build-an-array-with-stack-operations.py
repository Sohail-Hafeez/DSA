class Solution(object):
    def buildArray(self, target, n):
        j = 1
        output = []
        stream = []
        # Make the stream from 1 to n
        while j <= n:  # changed < n to <= n
            stream.append(j)
            j = j + 1
        j = 0
        for i in stream:
            if j >= len(target):  # stop when target is complete
                break
            if i == target[j]:
                output.append("Push")
                j = j + 1
                continue
            else:
                output.append("Push")
                output.append("Pop")
        return output
