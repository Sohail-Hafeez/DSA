class Solution:
    def removeLeadingSpaces(self, s: str) -> str:
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        return s[i:]

    def myAtoi(self, s: str) -> int:
        s = self.removeLeadingSpaces(s)

        if not s:
            return 0

        sign = 1
        i = 0
        answer = 0

        # handle sign only at first character
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        # read digits only
        while i < len(s) and s[i].isdigit():
            answer = answer * 10 + int(s[i])
            i += 1

        answer *= sign

        # clamp to 32-bit integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if answer < INT_MIN:
            return INT_MIN
        if answer > INT_MAX:
            return INT_MAX

        return answer