# 클래스 상속 & 메소드 재정의 연습

#Animal class

class Animal():
    age =0
    leg= 4
    color = ''
    species=''

    def __init__(self, age, leg, color, species):
        self.age = age
        self.leg = leg
        self.color = color
        self.species = species

    def talk(self):
        print('specific sounds')

    def eat(self):
        print('eating')

    def sleep(self):
        print('sleeping')

class Dog(Animal):
    def talk(self):
        print('woof woof')

    def eat(self):
        print('Dog is eating')

    def sleep(self):
        print('Dog is sleeping')

class Cat(Animal):
    def talk(self):
        print('meow meow')

    def eat(self):
        print('Cat is eating')

    def sleep(self):
        print('Cat is sleeping')

# dog1 = Dog()
# cat1 = Cat()
# dog1.talk()
# cat1.talk()


# 다형성 : 같은 이름의 메서드가 다른 기능
animals = [Cat(1,3,'white','A'), Cat(1,3,'red', 'B'), Dog(2,4,'black','d1')]

for animal in animals:
    animal.talk()