class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L =0
        R =0
        space = 0
        for i in moves:
            if i == "L":
                L = L+1
            elif i == "R":
                R = R+1
            else:
                space =space +1
        if L > R:
            return L+space-R
        else:
            return R+space - L