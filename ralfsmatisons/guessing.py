import random

value=raw_input("Enter a value between 1 and 10 ")
rnd=random.randint(1,10)
if (value== rnd):
    print("You have guessed the value")
else:
    print("Didnt guess")
