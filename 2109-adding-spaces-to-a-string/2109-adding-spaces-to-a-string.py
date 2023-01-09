class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = []
        spaces= set(spaces)
        if 0 in spaces:
            output.append(" ")
        for i in range(len(s)):
            output.append(s[i])
            if (i+1) in spaces:
                output.append(" ")
        return "".join(output)
        