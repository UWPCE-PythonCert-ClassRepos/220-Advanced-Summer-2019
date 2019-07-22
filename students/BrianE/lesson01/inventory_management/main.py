""" Launches the user interface for the inventory management system """

import sys
from inventory_management.market_prices import get_latest_price
from inventory_management.InventoryClass import InventoryClass
from inventory_management.FurnitureClass import FurnitureClass
from inventory_management.ElectricAppliancesClass import ElectricAppliancesClass


# Dictionary to store inventory data
FULL_INVENTORY = {}


def main_menu(user_prompt=None):
    """
    Prompt user for desired inventory related task
    :param user_prompt: string
    :return: call helper function
    """
    valid_prompts = {"1": add_new_item,
                     "2": item_info,
                     "q": exit_program}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        options_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
        print(f"Please choose from the following options ({options_str}):")
        print("1. Add a new item to the inventory")
        print("2. Get item information")
        print("q. Quit")
        user_prompt = input(">")
    return valid_prompts.get(user_prompt)


def get_price(item_code):
    """
    Get price data
    :param item_code: integer
    :return: floating point
    """
    return get_latest_price(item_code)


def add_new_item(full_inventory):
    """
    Add new item to inventory
    :return: None
    """
    item_code = input("Enter item code: ")
    item_description = input("Enter item description: ")
    item_rental_price = input("Enter item rental price: ")

    # Get price from the market prices module
    item_price = get_latest_price(item_code)

    is_furniture = input("Is this item a piece of furniture? (Y/N): ")
    if is_furniture.lower() == "y":
        item_material = input("Enter item material: ")
        item_size = input("Enter item size (S,M,L,XL): ")
        new_item = FurnitureClass.Furniture(item_code, item_description,
                                            item_price, item_rental_price,
                                            item_material, item_size)
    else:
        is_electric_appliance = \
            input("Is this item an electric appliance? (Y/N): ")
        if is_electric_appliance.lower() == "y":
            item_brand = input("Enter item brand: ")
            item_voltage = input("Enter item voltage: ")
            new_item = \
                ElectricAppliancesClass.ElectricAppliances(item_code,
                                                           item_description,
                                                           item_price,
                                                           item_rental_price,
                                                           item_brand,
                                                           item_voltage)
        else:
            new_item = InventoryClass.Inventory(item_code, item_description,
                                                item_price, item_rental_price)
    full_inventory[item_code] = new_item.return_as_dictionary()
    print("New inventory item added")


def item_info(full_inventory):
    """
    Input new item into inventory
    :return: None
    """
    item_code = input("Enter item code: ")
    if item_code in full_inventory:
        print_dict = full_inventory[item_code]
        for key, value in print_dict.items():
            print("{}:{}".format(key, value))
    else:
        print("Item not found in inventory")


def exit_program(full_inventory):
    """
    Exit program
    :return: system exit
    """
    print(f"Exiting with inventory:\n{full_inventory}")
    sys.exit()


if __name__ == '__main__':
    while True:
        print(FULL_INVENTORY)
        main_menu()(full_inventory=FULL_INVENTORY)
        input("Press Enter to continue...........")
