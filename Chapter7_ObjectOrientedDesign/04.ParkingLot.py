"""Parking Lot

Design a parking lot using object-oriented principles.

Hints: 
#258
Does the parking lot have multiple levels? What "features" does it support? Is it paid?
What types of vehicles?
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self.parking_spot = list()
        self.spot_needed = None
        self.size = None
    
    def get_spot_needed(self):
        return self.spot_needed
    
    def get_size(self):
        return self.size
    
    def park_in_spot(self, spot):
        self.parking_spot.append(spot)
    
    def clear_spot(self):
        for i in range(len(self.parking_spot)):
            self.parking_spot[i].remove_vehicle() 
        self.parking_spot.clear()
    
    @abstractmethod
    def can_fit_in_spot(self, spot):
        pass
    
    @abstractmethod
    def print_spots(self):
        pass


class VehicleSize:
    size_value = {"Motorcycle": 0, "Compact":1, "Large":2}

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__()
        self.spot_needed = 1
        self.size = VehicleSize.size_value["Motorcycle"]
    
    def can_fit_in_spot(self, spot):
        return True
    
    def print_spots(self):
        print("M")


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.spot_needed = 1
        self.size = VehicleSize.size_value["Compact"]
    
    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.size_value["Compact"] or \
                spot.get_size() == VehicleSize.size_value["Large"]
    
    def print_spots(self):
        print("C")


class Bus(Vehicle):
    def __init__(self):
        super().__init__()
        self.spot_needed = 5
        self.size = VehicleSize.size_value["Large"]
    
    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.size_value["Large"]
    
    def print_spots(self):
        print("B")


class ParkingSpot:
    def __init__(self, level, row, spot_number, spot_size, vehicle=None):
        self.level = level
        self.row = row
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle = vehicle
    
    def is_available(self):
        return self.vehicle is None
    
    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park(self, vehicle):
        if not self.can_fit_vehicle(vehicle):
            return False
        self.vehicle = vehicle
        self.vehicle.park_in_spot(self)
        return True
    
    def remove_vehicle(self):
        self.level.spot_freed()
        self.vehicle = None
    
    def get_row(self):
        return self.row
    
    def get_spot_number(self):
        return self.get_spot_number

    def get_size(self):
        return self.get_size


class Level:
    SPOTS_PER_ROW = 10
    def __init__(self, floor, spots_number):
        self.floor = floor        
        self.large_spots = spots_number // 4
        self.bike_spots = spots_number // 4
        self.compact_spots = spots_number - self.large_spots - self.bike_spots
        self.spots = list()
        for i in range(spots_number):
            spot_size = VehicleSize.size_value["Motorcycle"]            
            if i < self.large_spots:
                spot_size = VehicleSize.size_value["Large"]
            elif i < self.large_spots+self.compact_spots:
                spot_size = VehicleSize.size_value["Compact"]
            self.spots.append(ParkingSpot(self, i//self.SPOTS_PER_ROW, i, spot_size))
        self.available_spots = spots_number
    
    def get_available_spots(self):
        return self.available_spots
    
    def park_vehicle(self, vehicle):
        if self.get_available_spots() < vehicle.get_spot_needed():
            return False
        spot_number = self.find_available_spots(vehicle)
        return False if spot_number < 0 else self.park_starting_at_spot(spot_number, vehicle)
    
    def find_available_spots(self, vehicle):        
        last_row = -1
        spots_found = 0
        for i in range(len(self.spots)):
            spot = self.spots[i]
            if last_row != spot.get_row():
                spots_found = 0
                last_row = spot.get_row()
            if spot.can_fit_vehicle(vehicle):
                spots_found += 1
            else:
                spots_found = 0
            if spots_found == vehicle.get_spot_needed():
                return i - (vehicle.get_spot_needed()-1)
        return -1
    
    def park_starting_at_spot(self, spot_number, vehicle):
        vehicle.clear_spot()
        is_success = True
        for i in range(spot_number, spot_number+vehicle.get_spot_needed()):
            is_success = is_success & self.spots[i].park(vehicle)
        self.available_spots -= vehicle.get_spot_needed()
        return is_success


class ParkingLot:
    NUM_LEVEL = 3
    NUM_SPOTS = 10
    
    def __init__(self):
        self.levels = [Level(i, self.NUM_SPOTS) for i in range(self.NUM_LEVEL)]
    
    def park_vehicle(self, vehicle):
        for i in range(len(self.levels)):
            return self.levels[i].park_vehicle(vehicle)
        return False


from random import randrange

if __name__ == "__main__":
    parking_lot = ParkingLot()
    vehicle = Motorcycle()
    while parking_lot.park_vehicle(vehicle):
        random_num = randrange(0, 10)
        if random_num < 4:
            vehicle = Motorcycle()
        elif random_num < 7:
            vehicle = Car()
        else:
            vehicle = Bus()
        print("parked vehicle")
    print("full of parking lot")
