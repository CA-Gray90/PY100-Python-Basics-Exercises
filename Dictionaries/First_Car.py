car = {
    'type' :    'sedan',
    'color':    'blue',
    'mileage':  80_000,
}

print(car)

car['year'] = 2003
print(car)

# del car['mileage']
# print(car)

print(car.pop('mileage'))
print(car)

print(car['color'])
print(car.get('mileage', 'Item not in Dictionary'))

print(len(car))
print(len(car.items())) # .items() returns a dictionary view list object that contains a list of the key value pairs