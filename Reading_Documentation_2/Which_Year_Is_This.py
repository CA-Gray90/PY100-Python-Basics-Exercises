from datetime import date

today = date.today() # Method that returns the current local time

today_year = today.year # Returns an object representing the current year as an integer

iso_year = today.isocalendar()[0] # isocalendar returns a tuple with 3 components; year, week number, and weekday number. e.g. (year=2024, week=44, weekday=3)
                                  # Here we are assigning iso_year to the value at index 0 of the tuple
                                  # that is returned by .isocalender, which is the integer object representing the year (2024). 
                                  # Note that the isocalendars first week starts on the Monday of the first calendar week that contains a Thursday. 

print(today_year)
print(iso_year)