print("::CACULATOR::")
print("WELCOME TO MY FIRST CACULATOR")
print("enter the first number")
n1=input()
print("enter the operator")
n2=input()
print("enter the second number")
n3=input()
if n2=="+":
	print("sum of these two numbers is " , int(n1) + int(n3))
elif n2=="-":
	print("subtraction of these two numbers is" , int(n1) - int(n3))
elif n2=="/":
	print("division of these two numbers is ", int(n1)/int(n3))
elif n2=="*" :
	print("multiplication of these two numbers is " , int(n1)*int(n3))
elif n2=="%":
	print("modulus of these two numbers is ", int(n1)*int(n3)/100)
else:
	print("please enter a valid detais")
