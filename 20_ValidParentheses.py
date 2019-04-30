class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        stack = []
        symbols = {'(':')','{':'}','[':']'}
        keys = list(symbols.keys())
        values = list(symbols.values())
        for one in s:
            if one in keys:
                stack.append(one)
            else:
                if stack == []:
                    return False
                top = stack.pop()
                if symbols[top] != one:
                    return False
        if stack != []:
            return False
        return True

