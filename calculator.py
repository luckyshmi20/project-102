def calculate(option):
  if(option == '1' or option == '2'):
   num1 = float(input("enter a number"))
   num2 = float(input("enter another number")) 
   if option == '1':
    print(num1 + num2)
   elif option == '2':
    print(num1 - num2) 
   elif option == '3':
    print(num1 * num2)
   elif option == '4':
    print(num1 / num2) 

print("choose operation from below:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
option = input("enter option number (1/2/3/4)")
calculate(option)