# 1) The first bug i was looking for was finding if my logic was wrong. i wanted to
check if i was putting the wrong percentage decimal.
# 2) The function calculates the price after a discount was put on based on their
membership. It uses the price and tier variables to determine how big their
membership discount is and returns the final price after discount.
# 3) No AI used.
# Exercise 1
# Define calculate tax function
def calculate_tax(price, rate):
return price * rate
# Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
# Exercise 2
def apply_discount(price, tier):
if tier == "gold":
return price * 0.85
elif tier == "silver":
return price * 0.90
elif tier == "bronze":
return price * 0.95
else:
return price
# calling the function
price = 200
tiers = ["gold", "silver", "bronze", "none"]
for tier in tiers:
print(f"{tier}: ${apply_discount(price, tier):.2f}")
# Exercise 3
# Write it out manually first, then refactor into a function
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")
# Refractor into a function
def final_price(price, tier, tax_rate):
discounted = apply_discount(price, tier)
tax = calculate_tax(discounted, tax_rate)
return discounted + tax
print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")
# Exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
total = final_price(price, tier, 0.07)
print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")
# Exercise 6:
x = 100
def double_it(): # apple # Global
global x
# x = 999 # local another apple (not the same apple as above)
return x * 2
print(x)
print(double_it())
print(x)
