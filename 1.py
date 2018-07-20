import time
import random
i=0
door=30
while i>door:
  G =input（"走吗?(y/n),q=quit")
  if G="q":
    exit()
  elif g=="y":
    i=+randint(1,6)
    if i==door:
      print("到了！")
      exit()
    elif i>door:
      break()
    else:
      time.sleep(0)
print("坏人发现了你……")
