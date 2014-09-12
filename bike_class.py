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
        super(Frame, self).__init__(name, weight, production_cost)
        #Product.__init__(name, weight, production_cost)

        acceptable_materials = ("aluminum", "steel", "carbon")

        print name

        if frame_material in acceptable_materials:
             self.frame_material = frame_material
        else:
            print "You entered an unacceptable material, your bike frame was not created"


class Bike(Product):
    def __init__(self, name, wheels, frame, manufacturer_name):
        self.name = name
        self.wheels = wheels
        self.frame = frame
        self.manufacturer_name = manufacturer_name

        print frame.name

    def get_bike_weight(self):
        total_weight = self.wheels.weight + self.frame.weight
        return total_weight

    def get_bike_production_cost(self):
        total_cost = self.wheels.production_cost + self.frame.production_cost
        return total_cost



class SupplyChain(list):
    def get_selling_price():
        cost = 0
        for supplier in self:
            # define cost to contain margin
            cost += supplier.cost
        return cost


# my_chain = SupplyChain()
# my_chain.append(manufacturer_1)
# my_chain.append(bike_1)
# my_chain.append(customer_1)

#my_chain.get_cost()


class Business(object):
    #product is a bike object
    def __init__(self, name, cost):
        # a dict of bikes and their prices
        # this should maybe be a dict
        self.catalog = {}
        self.name = name
        self.cost = cost


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
        #for item in self.catalog:



class Bike_Shop(Business):
    pass



class Customer(object):
    pass

if __name__ == "__main__":
    my_wheel = Wheel("fat wheel", 10, 10)
    my_frame = Frame("alum5000", 10, 15, "aluminum")
    my_bike = Bike("tesla-cylce", my_wheel, my_frame, "Josh's bike supply")

    print "Bike weight = ", my_bike.get_bike_weight()
    print "Bike production cost = ", my_bike.get_bike_production_cost()





















