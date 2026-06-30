# 🅿️ Mini Practice – Vehicle Parking Slot Tracker

A smaller, confidence-building problem before you go back to the Library project. This is also a classic *baby version* of a real LLD interview question (Parking Lot), so it doubles as prep.

## 🎯 Objective

Model a tiny parking lot that tracks vehicles parking in and leaving numbered slots.

Practices: instance vs class variables, instance methods, class methods, static methods, `__str__`, `__repr__`, `__len__`, basic composition (a `ParkingLot` holds `Slot` objects).

---

## Requirements

### 1. `Vehicle` class

**Attributes**
- `number_plate`
- `vehicle_type` (e.g. `"car"`, `"bike"`)

**Dunder**
- `__str__` → e.g. `"Car - KA01AB1234"`

---

### 2. `Slot` class

**Attributes**
- `slot_number`
- `vehicle` (set to `None` when empty)

**Methods**
- `is_empty()` → returns `True`/`False`
- `park_vehicle(vehicle)` → assigns vehicle to slot; should refuse if slot is already occupied
- `unpark_vehicle()` → removes vehicle from slot, returns the vehicle that left

---

### 3. `ParkingLot` class

**Class variable**
```python
total_slots_created = 0
```
Increment this every time a `Slot` is created anywhere (hint: this means the increment logic actually belongs inside `Slot.__init__`, not `ParkingLot` — think about *why*).

**Attributes**
- `slots` — a list of `Slot` objects

**Methods**
- `add_slot(slot)` — adds a slot to the lot
- `park(vehicle)` — finds the **first empty slot** and parks the vehicle there; if no slots are free, print a message instead of crashing
- `unpark(number_plate)` — finds the slot containing that vehicle (by plate) and frees it
- `display_status()` — prints every slot number and whether it's empty or occupied (and by what plate, if occupied)

**Dunder**
- `__len__()` on `ParkingLot` → should return the **number of currently occupied slots** (not total slots — that's a deliberate twist, think about why `len()` returning "occupied count" might be more useful to a caller than "total slots")

---

### 4. Static method

On `ParkingLot`, add:
```python
@staticmethod
def is_valid_plate(plate)
```
Return `True` if the plate is a non-empty string with no spaces, `False` otherwise. (No need for real-world regex — keep it simple.)

---

### 5. Class method

On `ParkingLot`, add:
```python
@classmethod
def empty_lot(cls, num_slots)
```
A convenience constructor that builds a `ParkingLot` and pre-fills it with `num_slots` empty `Slot` objects (numbered 1 to `num_slots`), then returns it.

---

## Example Usage (should run without errors when done)

```python
lot = ParkingLot.empty_lot(3)

car = Vehicle("KA01AB1234", "car")
bike = Vehicle("KA02XY5678", "bike")

lot.park(car)
lot.park(bike)

lot.display_status()

print(len(lot))   # should print 2 (occupied slots)

lot.unpark("KA01AB1234")

lot.display_status()

print(len(lot))   # should print 1

print(ParkingLot.is_valid_plate("KA01AB1234"))   # True
print(ParkingLot.is_valid_plate(""))             # False

print(ParkingLot.total_slots_created)   # should print 3
```

---

## Self-Check Before Moving On

- [ ] `Slot.park_vehicle` refuses to overwrite an already-occupied slot
- [ ] `ParkingLot.park` handles the "lot full" case without crashing
- [ ] `__len__` counts *occupied* slots, not total slots — make sure you didn't just `return len(self.slots)`
- [ ] `empty_lot` is called on the class (`ParkingLot.empty_lot(3)`), not on an instance
- [ ] `is_valid_plate` is called without creating an instance first

---

## Why this problem (for LLD interview prep specifically)

Parking Lot is one of the most commonly asked LLD warm-up questions. This mini version isolates the OOP mechanics (so you build confidence with syntax) without yet pulling in the harder LLD concerns (multiple vehicle/slot types, pricing strategies, concurrency) — those come later once the basics are automatic.
