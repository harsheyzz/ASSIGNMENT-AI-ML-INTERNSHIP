num1=float(input("enter a number:"))
num2=float(input("enter another number:"))
print("press 1 for addition \n press 2 for subtraction \n press 3 for division \n press 4 for multiplication")
choice=int(input("enter your choice from 1-4:"))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1/num2)
elif choice==4:
    print(num1*num2)
else:
    print("ERROR")
