total_price = 0
rate = 0.9
items = int(input(":"))
while items <= 0:
    print("invalid value")
    items = int(input(":"))
for i in range (items):
    price_of_item = float(input("Price of item : $"))
    total_price += price_of_item
if total_price >= 100:
   total_price = total_price * rate
print(f"total price for {items} items is {total_price:.2f}")