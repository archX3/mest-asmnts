class Person:
    def __init__(self, name) :
        self.__name = name

    def get_name(self):
        return self.__name

    def __repr__(self):
        return self.__name

class Driver(Person):
    def __init__(self, name):
        super().__init__(name)

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

class SchoolBus:
    def __init__(self):
        self.__driver = None
        self.__students = []

    def can_drive(self):
        return len(self.__students) == 10 and not self.__driver == None

    def drive(self):
        if self.can_drive():
            print("vvvrrrrrooooooommmmmmmm")
        else:
            print("sorry man can't move")

    def add_driver(self, driver):
        if self.__driver == None:
            self.__driver = driver
            return "driver's name is {}".format(driver.get_name())
        else:
            return "we already have a driver"

    def add_student(self, student):
        if(len(self.__students) < 10):
            self.__students.append(student)
            return "student's name is {}".format(student.get_name())
        else:
            return "sorry our bus is full"

sch_bus = SchoolBus()

print(sch_bus.add_driver(Driver("Andrew PHP Berkowitz")))
print(sch_bus.add_driver(Driver("Andrew PHP Berkowitz")))

print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))
print(sch_bus.add_student(Student("Francis")))


