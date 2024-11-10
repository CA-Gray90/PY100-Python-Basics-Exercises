name = 'Roger'

comparison_string = 'RoGeR'

print(True if name.lower() == comparison_string.lower() else False)

comparison_string = 'DAVE'

print(name.casefold() == comparison_string.casefold())