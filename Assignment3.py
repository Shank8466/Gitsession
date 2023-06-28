# Calculator using arithmetic operators

choice = int(input("Enter your choice you want to perform: "))
a = int(input("Enter the number: "))
b = int(input("Enter the second number: "))

if (choice==1):
    print("Numbers after Addition: ",a+b)
elif(choice==2):
    print("Numbers after Subtraction",a-b)
elif(choice==3):
    print("Numbers after Division: ",a/b)
elif(choice==4):
    print("Numbers after Multiplication: ",a*b)
elif(choice==5):
    print("Numbers after Getting remainder: ",a%b)
else:
    print("!!Invalid Number!!")
    