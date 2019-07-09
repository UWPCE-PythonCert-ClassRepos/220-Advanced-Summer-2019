# Launches the user interface for the inventory management system
import sys
import market_prices
import inventoryClass
import furnitureClass
import electricAppliancesClass

def mainMenu(user_prompt=None):
    valid_prompts = {"1": addNewItem,
                     "2": itemInfo,
                     "q": exitProgram}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        options_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
        print("Please choose from the following options ({options_str}):")
        print("1. Add a new item to the inventory")
        print("2. Get item information")
        print("q. Quit")
        user_prompt = input(">")
    return valid_prompts.get(user_prompt)

def getPrice(itemCode):
    print("Get price")

def addNewItem():
    global fullInventory
    itemCode = input("Enter item code: ")
    itemDescription = input("Enter item description: ")
    itemRentalPrice = input("Enter item rental price: ")

    # Get price from the market prices module
    itemPrice = market_prices.get_latest_price(itemCode)

    isFurniture = input("Is this item a piece of furniture? (Y/N): ")
    if isFurniture.lower() == "y":
        itemMaterial = input("Enter item material: ")
        itemSize = input("Enter item size (S,M,L,XL): ")
        newItem = furnitureClass.furniture(itemCode,itemDescription,itemPrice,itemRentalPrice,itemMaterial,itemSize)
    else:
        isElectricAppliance = input("Is this item an electric appliance? (Y/N): ")
        if isElectricAppliance.lower() == "y":
            itemBrand = input("Enter item brand: ")
            itemVoltage = input("Enter item voltage: ")
            newItem = electricAppliancesClass.electricAppliances(itemCode,itemDescription,itemPrice,itemRentalPrice,itemBrand,itemVoltage)
        else:
            newItem = inventoryClass.inventory(itemCode,itemDescription,itemPrice,itemRentalPrice)
    fullInventory[itemCode] = newItem.returnAsDictionary()
    print("New inventory item added")


def itemInfo():
    itemCode = input("Enter item code: ")
    if itemCode in fullInventory:
        printDict = fullInventory[itemCode]
        for k,v in printDict.items():
            print("{}:{}".format(k,v))
    else:
        print("Item not found in inventory")

def exitProgram():
    sys.exit()

if __name__ == '__main__':
    fullInventory = {}
    while True:
        print(fullInventory)
        mainMenu()()
        input("Press Enter to continue...........")
