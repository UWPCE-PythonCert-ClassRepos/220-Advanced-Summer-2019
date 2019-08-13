from inventory_management.inventory_class import Inventory


class ElectricAppliances(Inventory):
    """ This class handles the Electric Appliances Object """

    def __init__(self, product_code, description, market_price, rental_price,
                 brand, voltage):
        # Creates common instance variables from the parent class
        self.brand = brand
        self.voltage = voltage
        super().__init__(product_code, description, market_price, rental_price)

    def return_as_dictionary(self):
        """ This returns a dictionary containing the expected fields """
        output_dict = super().return_as_dictionary()
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict