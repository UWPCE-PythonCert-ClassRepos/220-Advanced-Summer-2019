""" ElectricAppliances Class """


from inventory_management.InventoryClass import Inventory


class ElectricAppliances(Inventory):
    """
    This class manages electronic device details
    """

    def __init__(self, product_code, description, market_price,
                 rental_price, brand, voltage):
        # Creates common instance variables from the parent class
        Inventory.__init__(self, product_code, description,
                           market_price, rental_price)
        self.brand = brand
        self.voltage = voltage
