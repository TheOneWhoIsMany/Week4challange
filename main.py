import math
name = input("What is your name? ")
money = int(input("How much money have you made? "))
commissions = round((money * 0.13),2)
print(f"Your name is {name} and you are entitled to ${commissions} in commissions.")