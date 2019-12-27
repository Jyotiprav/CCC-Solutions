
s=input()
l=[]
for i in range(len(s)):
    for j in range(0,i):
        chunk =  s[j:i + 1]
        if chunk == chunk[::-1]:
            l.append(chunk)
print(len(max(l,key=len)))
