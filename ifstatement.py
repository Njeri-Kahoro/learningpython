#to check if a number is odd or even
num10 = int(input("Enter a number: "))
if num10 % 20 == 0:
    print(f'{num10} is even')
else:
    print(f'{num10} is odd')


age = int(input("How old are you? : "))
if age >= 18:
    print(f'{age} please proceed to voter registry')
else:
    print(f'{age} not eligible to vote')
