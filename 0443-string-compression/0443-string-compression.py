class Solution(object):
    def compress(self, chars):
        count = 1
        res = []

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
                continue

            elif count == 1:
                res.append(chars[i - 1])
            else:
                res.append(chars[i - 1])
                for c in str(count):
                    res.append(c)
                count = 1

        # Handle the last group
        if count == 1:
            res.append(chars[-1])
        else:
            res.append(chars[-1])
            for c in str(count):
                res.append(c)

        # Now copy res into chars in-place
        for i in range(len(res)):
            chars[i] = res[i]

        return len(res)
