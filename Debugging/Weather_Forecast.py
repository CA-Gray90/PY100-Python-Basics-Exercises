# Our predict_weather function should output a message indicating whether a sunny or cloudy day lies ahead. However, the output is the same every time the function is invoked. 
# Why? Fix the code so that it behaves as expected.

# import random

# def predict_weather():
#     sunshine = random.choice(['True', 'False'])   # variable sunshine will be assigned a string, 'True' or 'False' no Boolean value

#     if sunshine:                                  # Since sunshine is assigned a string, this will always evaluate to True (non-empty strings are Truthy)
#         print("Today's weather will be sunny!")
#     else:
#         print("Today's weather will be cloudy!")

                                                    # No invocation of the function

import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()