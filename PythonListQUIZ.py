#make list and print it
zoo = ["monkey", "elephant", "lion", "tiger", "giraffe"]
print(zoo)

#add panda to end of list
zoo.append("panda")
print("List after additions: ", zoo)

#print the number of animals
number_of_animals = len(zoo)
print("we now have", number_of_animals, "animals")

#delete the lion from the list
zoo.remove("lion")
print("After the lion escaped these are the animals in the zoo:", zoo)

#replace elephant with meerkat and print the list
zoo[1] = "meerkat"
print(zoo)
