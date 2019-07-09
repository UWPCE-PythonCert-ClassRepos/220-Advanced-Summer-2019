# Furniture class
from inventoryClass import inventory

class furniture(inventory):

    def __init__(self, productCode, description, marketPrice, rentalPrice, material, size):
        inventory.__init__(self,productCode,description,marketPrice,rentalPrice) # Creates common instance variables from the parent class

        self.material = material
        self.size = size

    def returnAsDictionary(self):
        outputDict = {}
        outputDict['productCode'] = self.productCode
        outputDict['description'] = self.description
        outputDict['marketPrice'] = self.marketPrice
        outputDict['rentalPrice'] = self.rentalPrice
        outputDict['material'] = self.material
        outputDict['size'] = self.size

        return outputDict