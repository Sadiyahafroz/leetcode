class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        word=list(word)
        count=0
        for n in range(len(word)):
            if word[n].isupper():
                count+=1
        if count == len(word):
            return True
        elif count==0:
            return True
        elif count==1:
            for n in range(len(word)):
                if word[0].isupper():
                    return True
                else:
                    return False
            