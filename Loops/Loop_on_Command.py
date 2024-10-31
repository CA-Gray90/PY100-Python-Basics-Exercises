# Modify the following code so the loop continues iterating until the user inputs 'yes'.

while True:
    print('Should I stop looping?')
    answer = input("Enter 'yes' to stop looping: ")
    if answer == 'yes':
        print('Thank God, exiting loop...')
        break
    print('Wrong input, entering another loop...')