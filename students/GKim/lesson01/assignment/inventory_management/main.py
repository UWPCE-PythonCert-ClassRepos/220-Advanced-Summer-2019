"""
Main Module
"""

# Launches the user interface for the inventory management system
import sys
import market_prices
import inventory_class
import furniture_class
import electric_appliances_class


def main_menu(user_prompt=None):
    """
    main menu
    """
    valid_prompts = {"1": add_new_item,
                     "2": item_info,
                     "q": exit_program}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        op_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
        print("Please choose from the following options ({}):"
              .format(op_str)
              )
        print("1. Add a new item to the inventory")
        print("2. Get item information")
        print("q. Quit")
        user_prompt = input(">")
        return valid_prompts.get(user_prompt)

def get_price(it_code):
    """
    get price method
    """
    print("Get price, {}".format(it_code))

def add_new_item():
    """
    add item method
    """
    global FULL_INVENTORY
    it_code = input("Enter item code: ")
    it_descrip = input("Enter item description: ")
    it_rent_price = input("Enter item rental price: ")

    # Get price from the market prices module
    item_price = market_prices.get_latest_price(it_code)

    is_furniture = input("Is this item a piece of furniture? (Y/N): ")
    if is_furniture.lower() == "y":
        item_material = input("Enter item material: ")
        item_size = input("Enter item size (S,M,L,XL): ")
        new_item = furniture_class.Furniture(it_code,
                                             it_descrip,
                                             item_price,
                                             it_rent_price,
                                             item_material,
                                             item_size
                                            )
    else:
        is_electric_appliance = input(
            "Is this item an electric appliance? (Y/N): ")
        if is_electric_appliance.lower() == "y":
            item_brand = input("Enter item brand: ")
            item_voltage = input("Enter item voltage: ")
            new_item = electric_appliances_class.ElectricAppliances(it_code,
                                                                    it_descrip,
                                                                    item_price,
                                                                    it_rent_price,
                                                                    item_brand,
                                                                    item_voltage
                                                                    )
        else:
            new_item = inventory_class.Inventory(it_code,
                                                 it_descrip,
                                                 item_price,
                                                 it_rent_price
                                                 )
    FULL_INVENTORY[it_code] = new_item.return_as_dictionary()
    print("New inventory item added")


def item_info():
    """
    item info method
    """
    it_code = input("Enter item code: ")
    if it_code in FULL_INVENTORY:
        print_dict = FULL_INVENTORY[it_code]
        for key, val in print_dict.items():
            print("{}:{}".format(key, val))
    else:
        print("Item not found in inventory")

def exit_program():
    """
    exit method
    """
    sys.exit()

if __name__ == '__main__':
    FULL_INVENTORY = {}
    while True:
        print(FULL_INVENTORY)
        main_menu()()
        input("Press Enter to continue...........")
