class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        f = s.split()
        d = len(f[-1])
        return d