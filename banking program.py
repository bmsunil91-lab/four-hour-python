
def show_balance():
  print(f"your balaence is ${balance:.2f}")
def deposite():
  amount=input("enter an amount to be deposited")
  return 0

  if amount<0:
    print("that's not a valid amount")
  else:
    return amount
def withdraw():
  amount=float(input("enter amount to be withdraw:"))

  if amount>balance:
    print("insufficient funds")
    return 0
  elif amount<0:
    print("amount must be grater than 0")
    return 0
  else:
    return amount
balance=0
is_running=True

while is_running:
  print("banking program")
  print("1.show balaence")
  print("2.deposite")
  print("3.withdraw")
  print("4.exit")

  choice=input("enter your choice(1-4):")

  if choice=='1':
    show_balance()
  elif choice=='2':
    balance+=deposite()
  elif choice=='3':
    balance-=withdraw()
  elif choice=='4':
    is_running=False
  else:
    print("that is not a valid choice")
print("thank you have a nice day")