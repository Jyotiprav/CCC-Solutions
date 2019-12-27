a,b=input().split(" ")
c,d=input().split(" ")
t=int(input())
min_step=abs(int(c)-int(a))+abs(int(d)-int(b))
if(min_step<=t):
    if((t-min_step)%2==0):
        print("Y")
    else:
        print("N")

else:
    print("N")
