# to round the final amount to 2 decimal points
import math

# create a list called menu
menu = ["cappuccino", "tea", "cheese and ham toastie", "soup", "orange juice", "chips"]

# create a dictionary containing the stock values for each item on menu
stock = {menu[0] : 0.40, 
         menu[1] : 0.20,
         menu[2] : 0.80,
         menu[3] : 0.70,
         menu[4] : 0.45,
         menu[5] : 0.30
         }

# create a dictionary containing the prices for each item
price = {menu[0] : 1.85,
         menu[1] : 1.10,
         menu[2] : 2.55,
          menu[3] : 2.20,
           menu[4] : 1.50,
           menu[5] : 1.60
}

# check for errors
for item in stock.items():
    print(item)

print()

for item in price.items():
    print(item)

print()

# define an item_value variable
item_value = 0

# define a total_stock variable
total_stock = 0

# loop through each item in menu to calculate the item_value 
# then calculate the total_stock value
for item in range(len(menu)):
    item_value = stock[menu[item]] * price[menu[item]]
    total_stock += item_value
    
print(f"The total cafe stock worth is: £{round(total_stock,2)}")
       