# Create as nested dictionary

# vehicles = {
#     'car' : {
#         'type' : 'sedan',
#         'color': 'blue',
#         'year' : 2003,
#     },
#     'truck' : {
#         'type' : 'pickup',
#         'color': 'red',
#         'year' : 1998,
#     },
# }
import pprint

# pprint.pp(vehicles)

# print(vehicles['truck']['color'])

# Another students solution, creates the dictionary from a series of lists with various attributes:
attributes = ['type', 'color', 'year']
car = ['sedan', 'blue', '2003']
truck = ['pickup', 'red', '1998']


car_dict = dict(zip(attributes, car))
print(car_dict)
truck_dict = dict(zip(attributes, truck))
print(truck_dict)
vehicles = dict([('car', car_dict), ('truck', truck_dict)])
pprint.pp(vehicles)