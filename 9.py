#PalindromicNumber
class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = []
        for n in str(x):
            l.append(n)
            h ="".join(l)

        j = l[::-1]
        k ="".join(j)
        if k == h:
            return True
        else:
            return False