# nested_car_list = [
#     ['type', 'sedan'],
#     ['color', 'blue'],
#     ['year', 2003],
# ]

vehicle_attributes = ['type', 'color', 'year']
car_details = ['sedan', 'blue', 2003]

nest_car_list = [list(element) for element in zip(vehicle_attributes, car_details)]

print(nest_car_list)

# nested_car_list = []
# index = 0
# for attribute in vehicle_attributes:
#     nested_car_list.append([attribute, car_details[index]])
#     index += 1

# print(nested_car_list)


# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# car_list = [
#     list(element) for element in car.items()
# ]

# print(car_list)