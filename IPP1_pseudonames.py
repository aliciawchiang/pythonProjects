#alicia chiang
#impractical python projects
# 1. silly name generation

import sys, random

print("Welcome to the psych 'sidekick name picket.'\n")
print("a name just like sean would pick for gus:\n\n")

first = ('baby oil', 'bad news', 'big burps')
last = ('appleyard', 'bigmeat', 'bloomshine')

while True:

    firstName = random.choice(first)
    lastName = random.choice(last)

    print("\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n")

    try_again = input("\n\nPress Enter to try again! Else n to quit)\n")
    
    if try_again.lower() == "n":

        break
    
input("\nPress Enter to exit.")