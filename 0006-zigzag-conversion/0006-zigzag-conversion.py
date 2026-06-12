class Solution:
    def horizontal(self, n, s, index, j, answer):
        for i in range(n):
            if index < len(s):
                answer[i][j] = s[index]
                index += 1
        return answer, index

    def zigzag(self, n, s, index, j, answer):
        i = n - 2
        while i > 0 and index < len(s):
            answer[i][j] = s[index]
            index += 1
            i -= 1
        return answer, index

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = numRows
        cols = len(s)  # safe upper bound

        answer = [['' for _ in range(cols)] for _ in range(n)]

        index = 0
        j = 0

        while index < len(s):
            answer, index = self.horizontal(n, s, index, j, answer)
            j += 1

            answer, index = self.zigzag(n, s, index, j, answer)
            j += 1

        # build result
        result = ""
        for i in range(n):
            for k in range(cols):
                if answer[i][k] != '':
                    result += answer[i][k]

        return result