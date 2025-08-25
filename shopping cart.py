foods=[]
prices=[]
total=0

while True:
  foods=input("enter the food to buy or (q to quit):")
  if foods.lower() == "q":
    break
  else:
    price=float(input(f"enter the price of {foods}:$"))
  foods.append(food)
  prices.append(price)

  print("------your cart------")
  for food in foods:
    print(food)

    for price in price:
      total+=price 
      print(f"your total price is:${total}")