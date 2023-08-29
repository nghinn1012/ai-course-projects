fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}

def getCostPerPound(fruit):
    """
    fruit: Fruit string
    Returns cost of 'fruit', assuming 'fruit'
    is in our inventory or None otherwise
    """
    if fruit not in fruitPrices:
        return None
    return fruitPrices[fruit]

def buyLotsOfFruit(orderList):
    """
    orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    totalCost = 0.0
    for fruit, numPounds in orderList:
        costPerPound = getCostPerPound(fruit)
        if costPerPound is None:
            print("Error: {} is not in the fruit inventory.".format(fruit))
            return None
        totalCost += numPounds * costPerPound
    return totalCost

# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
