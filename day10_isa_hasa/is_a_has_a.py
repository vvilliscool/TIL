#상속과 포함 관계 (has-a)

class Person:
    def __init__(self,name):
        self.name = name

    def greeting(self):
        print('Hi')

    def __repr__(self):
        return self.name
#상속관계
class Student(Person):
    def study(self):
        print('study')

class PersonList:
    def __init__(self):
        self.personList=[]

    def appendPerson(self, person):
        self.personList.append(person)

    def printInfo(self):
        for p in self.personList:
            print(p)

personL = PersonList()
nameL = ['Kim','Lee', 'choi']

for i in range(3):
    p = Person(nameL[i])
    # print(p)
    personL.appendPerson(Person(nameL[i]))

personL.printInfo()
