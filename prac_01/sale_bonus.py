"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
get sales
while sales >= 0
    calculate bonus
    get sales
do next thing
"""
bigger_or_equal_than_1000_rate = 0.15
lowwer_than_1000_rate = 0.1
sales = float(input("Enter sales: $"))
while sales >= 0:
   if sales >= 1000:
     bounes = sales * bigger_or_equal_than_1000_rate
   else:
     bounes = sales * lowwer_than_1000_rate
   print(bounes)
   sales = float(input("Enter sales: $"))
