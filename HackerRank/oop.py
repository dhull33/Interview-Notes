"""
Write a Person class with an instance variable, age, and a constructor that
takes an integer, initialAge, as a parameter. The constructor must assign
initialAge to age after confirming the argument passed as initialAge is not
negative; if a negative argument is passed as, initialAge, the constructor
should set age to 0 and print 'Age is not valid, setting age to 0.'. In
addition, you must write the following instance methods:

        1. yearPasses() should increase the  instance variable by 1 .
        2. amIOld() should perform the following conditional actions:
            If age < 13, print 'You are young.'.
            If age >= 13 and age < 18 , print 'You are a teenager.'.
            Otherwise, print 'You are old.'.
"""
class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            self.age = 0
            print('Age is not valid, setting age to 0.')
        else:
            self.age = initialAge

    def yearPasses(self):
        self.age += 1

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager')
        else:
            print('You are old')
