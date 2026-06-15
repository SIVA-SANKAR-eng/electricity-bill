class Equipment:
    def __init__(self, name, power, qty, hours):
        self.name = name
        self.power = power
        self.qty = qty
        self.hours = hours

    def connected_load(self):
        return self.power * self.qty

    def daily_energy(self):
        return (self.power * self.qty * self.hours) / 1000


fan = Equipment("Fan", 75, 5, 8)
led = Equipment("LED", 9, 8, 8)
tv = Equipment("TV", 120, 1, 3)
fridge = Equipment("Fridge", 200, 1, 12)
motor=Equipment("motor",750,1,1)
equipment_list = [fan, led, tv, fridge,motor]

total_load = 0
total_energy = 0

for item in equipment_list:
    load = item.connected_load()
    energy = item.daily_energy()

    print(f"{item.name}")
    print(f"Connected Load = {load} W")
    print(f"Daily Energy = {energy:.3f} kWh\n")

    total_load += load
    total_energy += energy

print("================================")
mec=total_energy*30
electricitybill=(mec*8)*2
print(f"Total Connected Load = {total_load} W")
print(f"Total Connected Load = {total_load/1000:.3f} kW")
print(f"Total Daily Energy = {total_energy:.3f} kWh")
print("================================")
print("YOUR MONTHLT ENERGY CONSUMPTION IS",mec)
print(f"PAYABLE AMOUNT IS",electricitybill,"Rs")