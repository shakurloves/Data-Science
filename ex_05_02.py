min = None
max = None
while True:
    ival = input('Enter Number: ')
    if ival == 'done' :
            break
    try:
        fval = float(ival)
    except:
        print('Invalid input')
        continue
    if min is None:
        min = fval
    elif min > fval :
        min = fval
    if max is None:
        max = fval
    elif max < fval :
        max = fval
#print('ALL DONE')
print('Maximum is', max,)
print('Minimum is', min,)
