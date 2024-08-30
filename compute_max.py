max = 0 #int input doesn't require int() for Ln 3
for i in [10, 2, 34, 6, 25,]:
    if i > max:
        max = i

print ('max value is', max)

max = '0'
for i in ['10', '2', '34', '6', '25',]:
    if int(i) > int(max): #requires int() when using str inputs i.e. quotation marks
        max = i

print ('max value is', max)