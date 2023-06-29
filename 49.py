class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l=[]
        licensePlate=list(licensePlate.split(" "))
        licensePlate="".join(licensePlate)
        for i in licensePlate:
            if i.isdigit() ==False:
                l.append(i.lower())
        
        shortest_word = None
        for word in words:
            for i in l:
                if i not in word or word.count(i) < l.count(i):
                    break
            else:
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word

        return shortest_word
                
                