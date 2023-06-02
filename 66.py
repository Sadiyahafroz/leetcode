class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        o = []
        for l in digits:
            l = str(l)
            o.append(l)
        print(o)
        d = "".join(o)
        print(d)
        d = int(d)
        d += 1
        print(d)
        d = str(d)
        print(d)# Convert to integer and then to string
        a = []
        for n in d:
            a.append(int(n))  # Convert each character to an integer
        return a
        

