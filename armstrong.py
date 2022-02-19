input = input("Enter a 3 digit Number: ")
input=int(input)
copyInput=int(input)

num1 = input%10 
input = input//10                 
num2= input%10

num3=input

cube=(num1*num1*num1)+(num2*num2*num2)+(num3*num3*num3)



if cube==copyInput: 
    print("Armstrong")

else:
    print("Not Armstrong")

