year = int(input('Enter a Year: '))

if(year%4 == 0 and year%400 == 0):
    print(year,"is leap year")
else:
    print(year,"id not leap year")