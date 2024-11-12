# Check whether the keys 'name' and 'grade' exist in the following dictionary:

student = {
    'id': 123,
    'grade': 'B',
}

key_check_list = ['name', 'grade']

# for key in keys_to_check:
#     print(f"'{key}' exists in the 'student' dictionary"
#           if student.get(key) else
#           f"'{key}' does not exist in the 'student' dictionary")

for key in key_check_list:
    print(f"'{key}' is in 'student' dict: {key in student}")
    
# def keys_to_check(dictionary, *args):
#     for arg in args:
#         print(f"'{arg}' exists in the 'student' dictionary"
#           if arg in dictionary else
#           f"'{arg}' does not exist in the 'student' dictionary")
        
# keys_to_check(student, 'name', 'grade')