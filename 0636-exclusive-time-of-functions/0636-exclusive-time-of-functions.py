class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        preTime = 0
        stack = []
        output = [0] * n

        for log in logs:
            id_str, state, time_str = log.split(":")
            id = int(id_str)
            currTime = int(time_str)

            if state == "start":
                if stack:
                    a = stack[-1]
                    output[a] += currTime - preTime   # FIX 1
                stack.append(id)
                preTime = currTime

            else:  # end
                a = stack.pop()
                output[a] += currTime - preTime + 1  # FIX 2
                preTime = currTime + 1               # FIX 3

        return output
