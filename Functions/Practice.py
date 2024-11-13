# Scope tests
def top():
    bottom()

def bottom():
    print('Bottom')

top()