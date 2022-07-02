#stock availabilaty checker

import random
import time
import os

true_false_random = 1, 2
result = random.choices(true_false_random)
os.system("cls")
print(result)

def main():
    time.sleep(2)
    if result == "1":
        print("stock not availabale")
    else:
        print("stock availabale")

main()

