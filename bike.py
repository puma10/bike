import bike_class

wheel_spoked = bike_class.Wheel("spoked", 4, 5.50)
wheel_thick = bike_class.Wheel("thick", 5, 6.50)

frame_alum_5000 = bike_class.Frame("alum_5000", 4, 25.00, "aluminum")
#frame_steel_2000 = bike_class.Frame("steel_2000", 5, 19.00, "steel" )


bike_tek = bike_class.Bike("bike_tek", wheel_spoked, frame_alum_5000, "manufacturer1")

print bike_tek.get_bike_weight
