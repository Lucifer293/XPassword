#Lucifer
#@7.7.6.6.1
import os
os.system("clear")
import random
import time
print("\033[32m")
print(" _       _   _   _____   _   _____   _____   _____   ")
print("| |     | | | | /  ___| | | |  ___| | ____| |  _  \  ")
print("| |     | | | | | |     | | | |__   | |__   | |_| |  ")
print("| |     | | | | | |     | | |  __|  |  __|  |  _  /  ")
print("| |___  | |_| | | |___  | | | |     | |___  | | \ \  ")
print("|_____| \_____/ \_____| |_| |_|     |_____| |_|  \_\ ")
time.sleep(0.9)
def XPassword(nnn):
 kkk = 20
 password = ''
 while len(password) != kkk:
  value = random.choice(nnn)
  password += value
 return password
nnn  = '012345678910'
for i in range (50000):
 print(XPassword(nnn))
