from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myCoffeeMachine = CoffeeMaker()
myMoneyMachine = MoneyMachine()
myMenu = Menu()

off = False

while not off:
    customerInput = input(f"What would you like to have? ({myMenu.get_items()}): ")
    if customerInput in ["latte", "espresso", "cappuccino"]:
        order = myMenu.find_drink(customerInput)
        if myCoffeeMachine.is_resource_sufficient(order) and myMoneyMachine.make_payment(order.cost):
            myCoffeeMachine.make_coffee(order)
    elif customerInput == "report":
        myCoffeeMachine.report()
        myMoneyMachine.report()
    elif customerInput == "off":
        print("Shutting down coffee machine...")
        off = True
    else:
        print("Invalid input. Please provide a valid input.")
