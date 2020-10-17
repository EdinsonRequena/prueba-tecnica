for i in range(1,101):
    if i %3 == 0 and i %5 == 0 and i %7 == 0:
        print('PlicPlacPloc') # Esta condicion se cumple si es divisible entre 3, 5 y 7

    elif i %3 == 0 and i%5 == 0:
        print('PlicPlac') # Esta condicion se cumple si es divisible entre 3 y 5

    elif i %3 == 0 and i %7 == 0:
        print('PlicPloc') # Esta condicion se cumple si es divisible entre 3 y 7

    elif i %5 == 0 and i %7 == 0:
        print('PlacPLoc') # Esta condicion se cumple si es divisible entre 5 y 7

    elif i %3 == 0:
        print('Plic') # Esta condicion se cumple si es divisible entre 3

    elif i %5 == 0:
        print('PLac') # Esta condicion se cumple si es divisible entre 5

    elif i %7 == 0:
        print('Ploc') # Esta condicion se cumple si es divisible entre 7

    else:
        print(i) # Si ninguna de las condiciones anteriores son ciertas impripira el numero correspondiente