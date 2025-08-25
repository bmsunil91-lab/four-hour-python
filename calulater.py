operater=input("enter the operater(+ - /):")
num1=float(input("enter the number:"))
num2=float(input("enter the number:"))
if operater ==("+"):
  result=num1+num2
  print(result)
elif operater==("-"):
  result=num1-num2
  print(result)
elif operater==("/"):
  result=num1/num2
  print(round(result))