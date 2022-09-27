# No of Multiples
l1= [1,2,3,4,5,6,7,8,9]
print(l1)
l2=[]

while True:
    elem= int(input("Enter the element: "))
    l2.append(elem)
    
    choice=input("To stop press'y', to Continue Press any key: ")
    if choice=="y":
        break
print(l2)

d={}
for i in range(0,len(l1)):
    count=0
    for j in range(0,len(l2)):
        if l2[j] % l1[i] ==0:
            count=count+1
    d[l1[i]]=count

print(d)