""" Furniture Class """


from inventory_management.InventoryClass import Inventory


class Furniture(Inventory):
    """
    This class manages furniture item details
    """

    def __init__(self, product_code, description, market_price,
                 rental_price, material, size):
        # Creates common instance variables from the parent class
        Inventory.__init__(self, product_code, description,
                           market_price, rental_price)
        self.material = material
        self.size = size
