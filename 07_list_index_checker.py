animals = ["Dog", "Cat", "Rabbit", "Duck", "Horse"] 


try:
    index = int(input("Enter an index: "))
    print(animals[index])
except IndexError:
    print("That index does not exist")
except ValueError:
    print("Enter a valid number (0-4)")