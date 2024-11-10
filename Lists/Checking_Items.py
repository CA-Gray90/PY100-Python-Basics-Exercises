# Write code that removes the items from grocery_list, one by one, printing them as we go, until it is empty.

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# while len(grocery_list) > 0:
#     print(grocery_list.pop(0))

# while grocery_list:
#     print(grocery_list.pop(0))

while grocery_list:             # Without using .pop(0)
    print(grocery_list[0])
    grocery_list = grocery_list[1:len(grocery_list)]

print(grocery_list)