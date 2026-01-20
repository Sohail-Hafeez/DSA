class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        j = 1
        count = 1
        flag = True
        while i<len(temperatures):
            while j<len(temperatures):
                if(temperatures[j]>temperatures[i]):
                    temperatures[i] = count
                    break
                j = j+1
                if(j>=len(temperatures) and flag):
                    temperatures[i] = 0
                    break
                count += 1
            i = i+1
            j=i+1
            count = 1
        temperatures[len(temperatures)-1] = 0
        return temperatures


class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)

        return ans

                    









