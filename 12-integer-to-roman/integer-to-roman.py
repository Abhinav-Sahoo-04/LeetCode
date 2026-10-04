class Solution:
    def intToRoman(self, n: int) -> str:
        maps={1:"I",4:"IV",5:"V",9:"IX",
          10:"X",40:"XL",50:"L",90:"XC",
          100:"C",400:"CD",500:"D",900:"CM",
          1000:"M"}
        maps=list(maps.items())
        length=len(str(n))
        div=10**(length-1)
        j=len(maps)-1
        res=""
        while n!=0:
            if maps[j][0]<=n:
                res+=maps[j][1]
                n-=maps[j][0]
            else:
                j-=1
        return res