'''class Human:
    height = 170
    satiety = 100

class Student(Human):
    satiety = 0

class Worker(Human):
    satiety = 100

nick = Student()
ann = Worker()
print(nick.height)
print(nick.satiety)
print(ann.height)
print(ann.satiety)'''

'''class Grandparent:
    height = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)

nick=Child()'''

'''class Wow:
    def __wow(self):
        print('Wow')
    def _hello(self):
        print('Hello')

some_obj=Wow()
some_obj.hello()
some_obj._Wow__wow()'''

'''
class Class1:
    var=20
    def __init__(self):
        self.var=10

class Class2(Class1):
    def __init__(self):
        print(self.var)
        super(Class2, self).__init__()
        print(self.var)
        print(super().var)
hello_world=Class()'''
'''
class Grandparent:
    def about(self):
        print('I am GrandParent')

    def about_myself(self):
        print('About meself Grandparent')

class Parent(Grandparent):
        def about_myself(self):
            print('I am Parent')

class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()

nick=Child()'''
'''
class computer:
    def calculate(self):
        print('Calculating...')

class Display:
    def display(self):
        print('I display the image on the screen...')

class Smartphone(Display, Computer):
    pass

iphone=Smartphone()
iphone.calculator()
iphone.display()'''
class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 12

class Display:
    def __init__(self):
        super().__init__()
         self.resolution='4K'

class Smartphone(Display, Computer):
    def print_into(self):
        print(self.resolution)
        print(self.memory)

pixel=Smartphone()
pixel.print_info()'''
