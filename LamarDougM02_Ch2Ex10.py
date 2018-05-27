cookies = int(input("How may cookies would you like to make?"))
# Using int, because I don't want an input of a negative or a floating point
# number

sugar = (cookies/48) * 1.5
butter = (cookies/48) * 1
flour = (cookies/48) * 2.75

#Trying to limit how long the numbers are to make a more reasonable answer
# i.e. I don't want an answer of '4.25343 cups of flour'
print("For", cookies, "cookies you will need", format(sugar, '.1f'),
      "cups of sugar,", format(butter, '.1f'), "cups of butter, and",
      format(flour, '.1f'), "cups of flour")

print("Doug Lamar")
