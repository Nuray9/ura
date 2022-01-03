from string import digits

number = input("Please enter a number between 0 and 99: ").strip()
#даем возможность вводить строку

result = ''

#используя string.digits, задаем длину от...до и ошибку
if (len(number) <= 0 or len(number) > 2) or (number[0] not in digits) or (len(number) == 2 and number[1] not in digits):
 print('Not right. ' 'You must enter a number between 0 and 99')
 exit()

if number[-1] == '0' and len(number) == 1:
    result = "zero"
if number[-1] == '1':
    result = 'one'
if number[-1] == '2':
    result = "two"
if number[-1] == '3':
    result = "three"
if number[-1] == '4':
    result = "four"
if number[-1] == '5':
    result = "five"
if number[-1] == '6':
    result = "six"
if number[-1] == '7':
    result = "seven"
if number[-1] == '8':
    result = "eight"
if number[-1] == '9':
    result = "nine"

#двухзначные числа
if len(number) == 2:
    if number == '10':
        result = 'ten'
    if number == '11':
        result = 'eleven'
    if number == '12':
        result = 'twelve'
    if number == '13':
        result = 'thirteen'
    if number == '14':
        result = 'fourteen'
    if number == '15':
        result = 'fifteen'
    if number == '16':
        result = 'sixteen'
    if number == '17':
        result = 'seventeen'
    if number == '18':
        result = 'eighteen'
    if number == '19':
        result = 'nineteen'

#десятки
    if number[0] == '2':
        result = "twenty " + result
    if number[0] == '3':
        result = "thirty " + result
    if number[0] == '4':
        result = "Fourty " + result
    if number[0] == '5':
        result = "fifty " + result
    if number[0] == '6':
        result = "sixty " + result
    if number[0] == '7':
        result = "seventy " + result
    if number[0] == '8':
        result = "eighty " + result
    if number[0] == '9':
        result = "ninety " + result


print(result)
