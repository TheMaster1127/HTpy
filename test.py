import random
# Define a dictionary to store dynamic variables
variables = {}


variables['ran'] = random.randint(1, 100)
for A_Index1 , value in enumerate(iter(int, 1), start=1):
    variables['A_Index1'] = A_Index1
    variables['userNum'] = int(input("guess a num form 1 to 100: "))
    variables['AIndex'] = str(variables['A_Index1'])
    if (variables['userNum'] == variables['ran']):
        print("You win in "  +  variables['AIndex']  +  " tries")
        break
    elif (variables['userNum']<variables['ran']):
        print("higher")
    else:
        print("lower")

