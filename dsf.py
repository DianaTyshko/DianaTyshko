'''try:
    print('start code')
    print(error)
    print('No errors')

except:
    print('We have an error')

print('Code after capsule')'''
'''try:
    print(10/0)
    print(error)
    
except NameError:
    print('u have NameError')
try:
    print(10/0)
except ZeroDivisionError:
    print('ZeroDivisionError')'''
'''
#ValueError
#ZeroDivisionError
try:
    a = int(input('first number'))
    b = int(input('second number'))
    c = a / b
    print(c)
except ValueError:
    print('not correct value')
except ZeroDivisionError:
    print(' U can not divide by error')'''

class computer:
    def calculate(self):
        print('Calculating...')

class Display:
    def display(self):
        print('I display the image on the screen...')

class Smartphone(calculator , display):
    pass

iphone = Smartphone()
iphone.calculator()
iphone.display()

try:
    a = int(input('first number'))
    b = int(input('second number'))
    c = a / b
    print(c)
except ValueError:
    print('not correct value')
except ZeroDivisionError:
    print(' U can not divide by error')

