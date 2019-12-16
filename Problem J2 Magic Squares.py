l=[]
l_inner=[]
for i in range(4):
    l_inner=[]
    a,b,c,d=input().split()
    l_inner.append(int(a))
    l_inner.append(int(b))
    l_inner.append(int(c))
    l_inner.append(int(d))
    l=l+[l_inner]
s=0
s_list=[]
for i in l:
    s=0
    for j in i:
        s=s+j
    s_list.append(s)
s1=0
s1_list=[]
for i in range(4):
    s1=0
    for j in range(4):
        s1=s1+l[i][j]
    s1_list.append(s1)

b=True
b1=True
for i in range(4):
    if s1_list[i]!=s1_list[0]:
        b=False
        break
for i in range(4):
    if s_list[i]!=s_list[0]:
        b1=False
        break
        
if s1_list==s_list and b and b1:
    print("magic")
else:
    print("not magic")
        
        

        
