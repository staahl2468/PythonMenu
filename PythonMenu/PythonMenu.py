


loop = True
tax = 1.08
total = 0


class FoodItem:
    def __init__(self, name, number, price, amount):
        self.name = name
        self.number = number
        self.price = price
        self.amount = amount


FoodItems = [FoodItem("Cheeseburger", 0, 35, 0), FoodItem("Hamburger", 1, 25, 0), FoodItem("Fries", 2, 20, 0), FoodItem("Small Soda", 3, 15, 0), FoodItem("Big Soda", 4, 20, 0)]
Order = [] 


for FoodItem in FoodItems:
    print('* {}-----     Press {}-----{}kr*'. format(FoodItem.name,FoodItem.number,FoodItem.price))
print("Press x to order")


while loop:
    
    choice = input("Please choose an item from the menu:")
    try:
        choice = int(choice)
    except:
        pass
    
    if choice == "x" or choice == "X":
        for FoodItem in Order:
            print("{} * {} = {}". format(FoodItem.name, FoodItem.amount, tax * round(FoodItem.price, 2) * FoodItem.amount, ))
        print(round(total))
        break
   
    amount = input("Please enter amount:")


    try:
        amount = int(amount)
        if amount > 10:
            print("You can order a maximum of 10 of each items per person")
            continue
    except:
        print("wrong input!")
        continue
    

    if isinstance(choice, int) and choice < len(FoodItems):
        total += FoodItems[choice].price * tax * amount
        FoodItems[choice].amount += amount
        if FoodItems[choice] not in Order:
            Order.append(FoodItems[choice])
        print(round(total, 2))

    else:
        print("You entered invalid item or amount")

