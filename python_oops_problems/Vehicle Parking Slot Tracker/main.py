# A model tiny parking lot that tracks vehicles in Parking in and leaving 

# Sol

class Vehicle:

  def __init__(self,number_plate,vehicle_type):
    self.number_plate = number_plate
    self.vehicle_type = vehicle_type
  
  def __str__(self):
    return (f"{self.vehicle_type} - {self.number_plate}")

class Slot:

  def __init__(self,slot_number,vehicle=None):
    self.slot_number = slot_number
    self.vehicle = vehicle
    ParkingLot.total_slots_created += 1

  def is_empty(self):
    return self.vehicle is None
  
  def park_vehicle(self,vehicle):
    if not self.is_empty():
      print("Unable to Park Vehicle in already occupied Slot")
    else:
      self.vehicle = vehicle
  
  def unpark_vehicle(self):
    departing = self.vehicle
    self.vehicle = None 
    return departing
  
class ParkingLot:
  total_slots_created = 0

  def __init__(self, slots=None):
    self.slots = slots if slots is not None else []

  def add_slot(self, slot):
    self.slots.append(slot)
  
  def park(self,vehicle):
    for slot in self.slots:
      if slot.is_empty():
        slot.park_vehicle(vehicle)
        print(f"Parked {vehicle} in slot {slot.slot_number}")
        return
    print("Parking lot is full")

  def unpark(self, number_plate):
    for slot in self.slots:
      if not slot.is_empty() and slot.vehicle.number_plate == number_plate:
        departing = slot.unpark_vehicle()
        print(f"{departing} has left slot {slot.slot_number}")
        return
    print(f"No vehicle with plate {number_plate} found")

  def display_status(self):
    for slot in self.slots:
      if slot.is_empty():
        print(f"Slot {slot.slot_number}: empty")
      else:
        print(f"Slot {slot.slot_number}: occupied by {slot.vehicle}")

  def __len__(self):
    return sum(1 for slot in self.slots if not slot.is_empty())

  @staticmethod
  def is_valid_plate(plate):
    return isinstance(plate, str) and len(plate) > 0 and " " not in plate

  @classmethod
  def empty_lot(cls, num_slots):
    lot = cls()
    for i in range(1, num_slots + 1):
      lot.add_slot(Slot(i))
    return lot
  
#INPUT
 
lot = ParkingLot.empty_lot(3)

car = Vehicle("KA01AB1234", "car")
bike = Vehicle("KA02XY5678", "bike")

lot.park(car)
lot.park(bike)

lot.display_status()
print(len(lot))

lot.unpark("KA01AB1234")
lot.display_status()
print(len(lot))

print(ParkingLot.is_valid_plate("KA01AB1234"))
print(ParkingLot.is_valid_plate(""))

print(ParkingLot.total_slots_created)