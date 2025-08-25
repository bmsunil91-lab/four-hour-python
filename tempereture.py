unit=input("enter the tempereture celsius or fahenheit (C/F)")
temp=float(input("enter the tempereture: "))

if unit=="C":
    temp=(9*temp)/5+32
    print(f"tempereture in fahenheit: {temp}")
elif unit=="F":
  temp=(temp-32)*5/9
  print(f"tempereture in celsius: {temp}")
else:
  print(f"{unit} is invalid ")