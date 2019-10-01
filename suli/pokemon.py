### First attempt

print("Hi there, welcome to Pokemon!")
name = raw_input("What is your name? ")
print("Hi Master " + str(name))
print(name + " pick a starter Pokemon, you can choose from Bulbasaur, Squirtle and Charmander.")
Bulbasaur = raw_input("Bulbasaur? ")
if Bulbasaur == "yes":
    print("You chose Bulbasaur\nThanks for playing, bye!")
    exit()
else:
    print("Ok")

Squirtle = raw_input("Squirtle? ")
if Squirtle ==  "yes":
    print("You chose Squirtle\nThanks for playing, bye!")
    exit()
else:
    print("Ok")

print("You chose Charmander\nThanks for playing, bye!")
