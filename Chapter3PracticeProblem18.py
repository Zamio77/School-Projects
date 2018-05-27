vegie = input("Is anyone in your party a vegitarian?")

vegan = input("Is anyone in your party a vegan?")

gluten = input("Is anyone in your party a gluten-free?")

if vegie == "Yes" and vegan == "Yes" and gluten == "Yes":
    print("Here are your restaurant choices")
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")

elif vegie == "Yes" and vegan == "No" and gluten == "Yes":
    print("Here are your restaurants")

else:
    print("Please enter a restaurant")
