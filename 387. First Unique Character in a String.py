class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ss in s:
            if s.count(ss)==1:
                return s.index(ss)
        return -1