class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence=set(sentence)
        s=set(chr(97+i) for i in range(27))
        count=0
        for i in sentence:
            if i  in s:
                count+=1
        return True if count>=26 else False
        