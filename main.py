# password must be between 8-12 characters, MUST have 2 upper and MUST have 3 lower case, digits 0-9

upper = False
lower = False
less = False
greater = False
digit = False
three_capital = False
count = 0
count2 = 0
two_lower = False

password = input('please enter a new password: ')

# check to see if upper and lower case exist in the list
for letter in password:
    if letter.isupper():
        upper = True
    elif letter.islower():
        lower = True
# check to make sure the length meets 8-12
    if len(password) >= 8 and len(password) <= 12:
        greater = True
        less = True
# Check to see if there is a # in there
for letter in password:
    if letter.isdigit():
        digit = True

# to check for 2 capital letters
for letter in password:
    count = sum(1 for letter in password if letter.isupper())
    if count < 2:
        three_capital = False
    elif count > 1:
        three_capital = True

# to check for 3 lowercase letters
for letter in password:
    count2 = sum(1 for letter in password if letter.islower())
    if count2 > 2:
        two_lower = True
    elif count2 < 3:
        two_lower = False
# the while loop is really 1 giant while true = valid statement
while (upper is True) and (lower is True) and (greater is True) and (less is True) and (digit is True)\
        and (three_capital is True) and (two_lower is True):
    print('Valid')
    break
else:
    print('Invalid')
