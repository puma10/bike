class Product(object):

    def __init__(self, name, weight, production_cost):
        self.name = name
        self.weight = weight
        self.production_cost = production_cost


class Wheel(Product):
    pass


class Frame(Product):
    # Just wanted to add frame_material param and inherit all other params from the Product class.  How do I do this?
    def __init__(self, name, weight, production_cost, frame_material):
        acceptable_materials = ("aluminum", "steel", "carbon")

        if frame_material in acceptable_materials:
             self.frame_material = frame_material
        else:
            print "You entered an unacceptable material"


class Bike(Product):
    def __init__(self, name, wheels, frame, manufacturer_name):
        self.name = name

    def get_bike_weight(self):
        total_weight = wheels.weight + frame.weight
        return total_weight

    def get_bike_production_cost(self, wheels_cost, frame_cost):
        total_cost = wheels.production_cost + frame.production_cost
        return total_cost




class Business(object):
    #product is a bike object
    def __init__(self, name):
        # a dict of bikes and their prices
        # this should maybe be a dict
        self.catalog = {}
        self.name = name



# trying to figure out how to use a parent class to represent the supply chain markup that is incurred everytime a product is passed from a manufacturer to a shop to a customer.  It is the same process.  A selling price = the new selling price plus the margin.

# supplier bike costs = $30


class Manufacturer(Business):
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin

     def add_bike(self, bike):
        # get the bikes cost of goods
        self.cost = bike.get_bike_production_cost

        #create/update selling price to reflect margin
        #selling price = cost / (1 - margin)
        self.selling_price = self.cost / (1 - self.margin)

        #calcuate new
        self.profit = self.selling_price - self.cost

        #add bike object to catalog
        self.catalog.append(bike)

        # iterate through each product in the companies catalog and update it's selling price to reflect the companies profit margin
        for item in self.catalog:




class Bike_Shop(Business):






















