arrival=input().split(":")
h=int(arrival[0])
m=int(arrival[1])
distance=0
while(distance<120):
    if(h>=7 and h<10):
        distance+=0.5
    elif(h>=15 and h<19):
        distance+=0.5
    else:
        distance+=1
    m=m+1
    if(m==60):
        m=0;
        h=h+1

    if(h==24):
        h=0

if(h<10):
    print('0',end="")
print(h,":",end="")
if(m<10):
    print("0",end="")
print(m,end="")
