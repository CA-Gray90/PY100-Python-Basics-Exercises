# Write a function that, without using the built-in `in` operator, checks whether a specific destination is included within destinations
# Must Return a boolean

# def contains(obj, collection):
#     for element in collection:
#         if obj == element:
#             return True
#     return False

# def contains(obj, collection):
#     result = [True for element in collection if element == obj]
#     return any(result)

# def contains(obj, collection):
#     return any([True for element in collection if element == obj])

def contains(obj, collection):
    return any(element == obj for element in collection)

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations)) # False