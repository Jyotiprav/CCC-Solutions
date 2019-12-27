question=int(input())
numpeople=int(input())

AP = [int(i) for i in input().split()][:numpeople]
BP = [int(i) for i in input().split()][:numpeople] 

AP.sort()
BP.sort()

if(question==1):
    min1=0
    for i in range(numpeople):
        min1+=max(AP[i],BP[i])
    print(min1)
elif(question==2):
    max1=0
    for i in range(numpeople):
        max1+=max(AP[i],BP[numpeople-i-1])
    print(max1)

