from collections import defaultdict
class Solution:
    def grams(self,str):
        anagrams=defaultdict(list)
        result=[]
        for s in str:
            sort=tuple(sorted(s))
            anagrams[sort].append(s)
        for val in anagrams.values():
            result.append(val)
        print(result)

sol=Solution()
str=['mad','dad','cat','man','tac','nam']
sol.grams(str)