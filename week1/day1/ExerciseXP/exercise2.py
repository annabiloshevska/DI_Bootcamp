print('Hello world\n'*4,'I love python\n'*4)

month=int(input('Enter a month(1 to 12): '))
if 3 <= month <= 5:
    print('It\'s spring')
elif 6 <= month <= 8:
    print('It\'s summer')
elif 9 <= month <= 11:
    print('It\'s autumn')
elif month == 12 or 1 <= month <=2:
    print('It\'s winter')
else:
    print('Invalid month')