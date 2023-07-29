#List
products_list = ["Magnolia Chicken","555 Sardines","Palmolive Soap","Sunsilk Shampoo","Tide Ultra","Gillette Blade"]

#Ask user input product name
search = input("Enter the Product to Search")

#if else statement to found the Product the user to seach
if search in products_list:
  print("\nProduct Found: ",search)
else:
  print("\nProduct not found: ",search)
