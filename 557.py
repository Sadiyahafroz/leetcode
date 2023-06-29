class Solution:
    def reverseWords(self, s: str) -> str:
        lst=list(s.split())
        for n in range(len(lst)):
            lst[n]=lst[n][::-1]
        sent=" ".join(lst)
        return sent

        