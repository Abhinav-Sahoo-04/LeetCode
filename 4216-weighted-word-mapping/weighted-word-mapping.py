class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        d=""
        for i in range(len(words)):
            total=0
            for j in range(len(words[i])):
                index=ord(words[i][j])-97
                total+=weights[index]
            total%=26
            d+=chr(97+25-total)
        return d

