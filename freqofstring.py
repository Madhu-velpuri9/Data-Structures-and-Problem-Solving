from  collections import Counter
def feqstring(s):
    count=Counter(s)
    for i,j in count.items():
        print(i,j)

s='jagadeeswar'
feqstring(s)
print(feqstring(s))


