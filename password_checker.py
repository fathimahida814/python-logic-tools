password = input('Please type a password')

if len(password) < 8:
    print('Too short')
has_number = False
for letter in password:
    if letter in '0123456789':
        has_number = True
if has_number == True:
    print('has number')
else:
    print('no number')
