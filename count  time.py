import time

my_time=int(input("enter the time in second: "))

for x in range(my_time,0,-1):
  second=x%60
  minute=int(x/60)%60
  hour=int(x/3600)%24
  print(f"{hour}:{minute:02}:{second:02}")
  time.sleep(1)
  print("TIME'S UP!")

  