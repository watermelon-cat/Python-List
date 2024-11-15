#creating list
gross_items = ["moldy sandwich", "stinky sock", "half-eaten banana", "mystery goo" ,"black licorish","purple slime","rotten apple"]

#get first and last idem in list
first_item = gross_items[0]
last_item = gross_items[-1]
print("the first item is a", first_item, "and the last item is ", last_item + ".")

# slice the list: copy a portion of it into another list
show_and_smell_items = gross_items[1:3]
print("the items coming for 'show and smell' are:", show_and_smell_items)

items_in_partners_lunch = gross_items[4:7]
print("he had ", items_in_partners_lunch, " in his lunch")


#swap a list items
gross_items[2] = "fly stuck in cheese"
print("Updated gross items:", gross_items)


#add elements
gross_items.append("mystery slime")
gross_items.insert(0, "sticky bandage")
print("list after adding items:", gross_items)

#remove elements
gross_items.remove("stinky sock")
slithering_item = gross_items.pop()
print("After some items left:", gross_items)

gross_items.remove("mystery goo")
print("items left:", gross_items)

#print list length
number_of_items = len(gross_items)
print("we now have", number_of_items, "gross items.")

#check if item is in list
has_mystery_goo = "rotten apple" in  gross_items
print("Do we still have rotten apple?")
if has_mystery_goo == True:
    print("yes!")
else:
    print("no")
    
#loop through list
for item in gross_items:
    print("Behold the incredibly gross", item, "!")
