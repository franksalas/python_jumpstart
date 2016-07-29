import random

print('---------------------------')
print('   guest the number game')
print('---------------------------')
print()

the_number = random.randint(0, 100)

guess = -1

while guess !=the_number:
    guest_text = input('guest a number between 0 and 100: ')
    guess = int(guest_text)

    if guess < the_number:
        print('too low')
    elif guess > the_number:
        print('too high')
    else:
        print('you win!')
