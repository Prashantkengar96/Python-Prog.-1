# Calculator
a=int(input("Enter a first number: "))
c=input("Enter Operator to perform task: ")
b=int(input("Enter a second number: "))

if c=="+":
    print("Your Answer is: ",a+b)
elif c=="-":
    print("Your Answer is: ",a-b)
elif c=="*":
    print("Your Answer is: ",a*b)
elif c=="/":
    print("Your Answer is: ",a/b)
else: 
    print("Please use + - * or / operators only")