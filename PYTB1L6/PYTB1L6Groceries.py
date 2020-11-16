GroceryList = ("milk", "bread", "bacon", "eggs", "cheese")

ShoppingCart = ("milk", "bread", "bacon", "cheese", "eggs")


for i in GroceryList:
    if ShoppingCart in GroceryList:
        print("Done Shopping")

    else:
        print("Continue Shopping")
        break
