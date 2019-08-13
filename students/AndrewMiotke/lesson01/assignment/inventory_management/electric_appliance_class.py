""" Electric appliances class """

from inventory_management.inventory_class import Inventory

class ElectricAppliances(Inventory):
    """
    Electric Appliances Class
    Inheriting from Inventory
    """

    def __init__(self,
                 product_code,
                 description,
                 market_price,
                 rental_price,
                 brand,
                 voltage):

        # Creates common instance variables from the parent class
        super().__init__(self,
                         product_code,
                         description,
                         market_price,
                         rental_price)


        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        """ Return a dictionary """

        output_dict = Inventory.return_as_dictionary(self)
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
