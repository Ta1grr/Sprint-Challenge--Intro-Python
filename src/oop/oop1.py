# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

"""" Parent(Base) Class """
class Vehicle():
    def __init__(self, name):
        self.name = name

""" Child Branch -- Vehicle >> GroundVehicle """
class GroundVehicle(Vehicle):
    def __init__(self, name):
        super().__init__()
    
""" Grandchild Branch -- Vehicle >> GroundVehicle >> Car """        
class Car(GroundVehicle):
    def __init__(self, name):
        super().__init__()

""" Grandchild Branch -- Vehicle >> GroundVehicle >> Motorcycle """
class Motorcycle(GroundVehicle):
    def __init__(self, name):
        super().__init__()

""" Child Branch -- Vehicle >> FlightVehicle """
class FlightVehicle(Vehicle):
    def __init__(self, name):
        super().__init__()

""" Groundchild Branch -- Vehicle >> FlightVehicle >> Starship """
class Starship(FlightVehicle):
    def __init__(self, name):
        super().__init__()

""" Groundchild Branch -- Vehicle >> FlightVehicle >> Airplane """
class Airplane(FlightVehicle):
    def __init__(self, name):
        super().__init__()