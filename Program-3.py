# Pattern 2
a=int(input("Enter a no: "))
print(a)
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j+(j-1),end=' ')
    print()
    for j in range(1,i+1):
        print(j+(j-1),end=' ')
    print()