class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        for ss in s:
            if ss.lower() in ["a","e","i","o","u"]:
                l.append(ss)
        l.reverse()

        n=0
        result=[]

        for i in range(len(s)):
            if s[i].lower() in ["a","e","i","o","u"]:
                result.append(l[n])
                n+=1
            else:
                result.append(s[i])

        return "".join(result)