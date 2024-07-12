import random

def coinflip(choice):
    print('Russian Roulet, You feeling lucky punk?')

    num = random.randint (1,2)

    if num == 1:
        result='Heads'

    elif num == 2:
        result='Tails'

    if choice==result:
        result_cf = 'Guess you live to see another day, lucky bastard!'

    else:
        result_cf = 'Motherfucker you dead!'

    print ('Get the fuck of my lawn ugly Motherfucker!')

    print (f'You chose: {choice} its: {result}. {result_cf}')
    return f'You chose: {choice} its: {result}. {result_cf}'




    
    
