class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        l=list(num[::-1])
        l2=[]
        for i in range(len(l)):
            if l[i]==str(0):
                print(l[i])
                continue
            else:
                print(l[i])
                l2.extend(l[i:])
                break
        l2=l2[::-1]
        l3= "".join(l2)
        return l3


        