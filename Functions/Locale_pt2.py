def extract_region(locale):
    return locale[3:5]

def extract_region(locale):
    if locale[2] == '_' and 'UTF-' in locale: # a locale code will have both a '_' at index 2 and 'UTF-' in it.
        region_index = locale.find('_') + 1
        return locale[region_index:region_index + 2]
    
    return 'Incorrect Locale Code'

# LS Solution:

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]


print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR
# print(extract_region('Australia'))      # Incorrect Locale Code