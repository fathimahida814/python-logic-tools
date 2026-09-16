total = 0
items = int(input('How many items?'))
for item in range(items):
    price = int(input('What is the price of item?'))
    total += price
print(total)