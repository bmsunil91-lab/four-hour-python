weight=float(input("enter the weight:"))
unit=input("kilograms or pounds? (K or L):")
if unit == "K":
  weight=weight * 2.205
  unit="lbs."
  print(f"your weight is: {round (weight)} {unit}" )
elif unit == "L":
  weight=weight / 2.205
  unit="kgs."
  print(f"your weight is: { round (weight),1} {unit}" )
else:
  print(f"{unit} not  vailad")