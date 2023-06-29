class Solution:
    def isValid(self, s: str) -> bool:
        for p in s:
            if "()"in s:
                
                s=s.replace("()","")
            elif "[]"in s:
                
                s=s.replace("[]","")
            elif "{}"in s:
                
                s=s.replace("{}","")
        if s=="":
            return True
        else:
            return False