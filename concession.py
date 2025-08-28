menu={
  "pizza":3.00,
  "popcone":2.00,
  "fries":2.50,
  "soda":3.00}
cart=[]
total=0

print("--------menu-----------")
for key,value in menu.items():
  print(f"{key:10}:{value:.2f}")
  print("------------------")
while True:
  food=input("Select an items(q to quit):").lower()
  if food =="q":
    break 
  elif menu.get(food) is not None:
      cart.append(food)
  print(cart)

print("---------your order--------")

for food in  cart:
     total+=menu.get(food)
     print(food,end="")
    
print()
print(f"total is :${total:.2f}")
  
     
     





