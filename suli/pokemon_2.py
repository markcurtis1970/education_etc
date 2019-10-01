print("Hi there, welcome to Pokemon!")
name = raw_input("What is your name? ")
print("Hi Master " + str(name))
choice  = raw_input("Pick a starter Pokemon:\n1 - Bulbasaur\n2 - Squirtle\n3 - Charmander\n")
if int(choice) == 1:
    print("You chose Bulbasaur\nThanks for playing, bye!")
    exit()
elif int(choice) == 2:
    print("You chose Squirtle\nThanks for playing, bye!")
    exit()
elif int(choice) == 3:
    print("You chose Charmander\nThanks for playing, bye!")
else:
    print("No valid choice made, please try again.")
exit()
