foods=[]
prices=[]
total=0
while True:
    food=input("Enter a food to buy (Press Nothing to quit):")
    if food=="":
        break
    else:
        price=float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
print("--------CART--------")
for food in foods:
    print(food)
for price in prices:
    total+=price
print(f"Total price is ${total}")