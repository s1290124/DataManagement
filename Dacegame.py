import random

print("What is your name?")
name = input(">")
print("Hello,{}!".format(name))

print("Rolling dace...")

roll1 = random.randint(1,6)
roll2 = random.randint(1,6)

total_value = roll1 + roll2

print("Die 1: ",roll1)
print("Die 2: ",roll2)
print("Total value: ",total_value)

if total_value > 7:
    print("{} won!".format(name))
else:
    print("{} lost".format(name))