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

has_capital = False
for letter in password:
    if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        has_capital = True
if has_capital == True:
    print('has capital')
else:
    print('no capital')

has_character = False
for letter in password:
    if letter in '!@#$%^&*':
        has_character = True
if has_character == True:
    print('has character')
else:
    print('no character')

if len(password) >= 8 and has_number and has_capital and has_character:
    print('Strong password')
else:
    print('weak password')