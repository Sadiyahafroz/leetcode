class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s=="":
            return True
        else:
            l=[]
            
            for ss in s.lower():
                if ss.isalpha():
                    l.append(ss.lower())
                elif ss.isdigit():
                    l.append(ss.lower())
            sss="".join(l)
            ssss=sss[::-1]
            if sss==ssss:
                return True
            else:
                return False