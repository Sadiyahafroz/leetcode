class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0

        for word in words.copy():
            print("pair: ", word)
            pair2 = str(word[::-1])
            print("pair2: ", pair2)
            if pair2 in words:
                if word == pair2:
                    print("removed", word, pair2)
                    words.remove(word)
                else:
                    print("removing both", word, "and", pair2)
                    words.remove(word)
                    words.remove(pair2)
                    count += 1

        return count