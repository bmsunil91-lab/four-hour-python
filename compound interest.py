principle=0
rate=0
time=0
while principle <=0:
  principle=float(input("enter the prinicple amount: "))
  if principle <=0:
   print("the principle can't be less than or equal to 0")

  while rate <=0:
   rate=float(input("enter the interast  rate: "))
   if rate <=0:
    print("the interest  can't be less than or equal to 0: ")

  while time <=0:
   time=int(input("enter the time in year: "))
   if time <=0:
    print("the time can't be less than or equal to 0: ")
total= principle *  pow((1+rate/100),time)
print(f"balance after {time} year/s:${total :.2f}")
  
  
  