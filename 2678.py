class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for inputs in details:
            if int(inputs[11:13])>60:
                count+=1
        return count
