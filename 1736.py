class Solution:
    def maximumTime(self, time: str) -> str:
        def pad(x):
            x = str(x)
            if len(x) < 2:
                x = '0' + x
            return x

        def match(a,b):
            for x,y in zip(a,b):
                if x == y or y == "?":
                    continue
                return False
            return True


        best = ''
        for hh in range(0,24):
            for ss in range(0,60):
                current = pad(hh) + ':' + pad(ss)

                if match(current,time):
                    best = current
        return best