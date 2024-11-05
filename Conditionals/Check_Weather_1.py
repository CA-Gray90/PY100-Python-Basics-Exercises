# Different weather strings: 'sunny', 'rainy', 'stormy', 'hurricane!', '40 plus degrees'
import random

weather_choices = ['sunny', 'rainy', 'stormy', 'a hurricane!', '40 plus degrees', 'windy']

weather = random.choice(weather_choices)
print(f'Outside it is {weather}')
match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella')
    case 'a hurricane!':
        print('For the love of God take shelter!')
    case _:
        print("Let's stay inside")

# if weather == 'sunny':
#     print("It's a beautiful day!")
# elif weather == 'rainy':
#     print('Grab your umbrella')
# else:
#     print("Let's stay inside")

# Another students solution:

# weather = ('rainy', 16)

# match weather:
#     case ('sunny', temp):
#         print(f"It's a beautiful day! The temperature is {temp} degrees.")
#     case ('rainy', temp) if temp > 15:
#         print(f"It's raining and warm. The temperature is {temp} degrees.")
#     case ('rainy', _):
#         print("Grab your umbrella.")
#     case _:
#         print("Let's stay inside.")