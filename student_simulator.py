import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progres = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progres += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progres -= 0.1

    def is_alive(self):
        if self.progres < -0.5:
            print('Cast out...')
            self.alive = False

        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False

        elif self.progres > 5:
            print('Passed externally...')
            self.alive = False
