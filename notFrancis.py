class Person:
    def __init__(self, name, gender):
        if(name == "Francis"):
            raise ValueError("what kind of horrible parent would name their child Francis?")
        else:
            self.__name = name
            self.__gender = gender

    def __repr__(self):
        return "This persons is a {} and named {}".format(self.__gender, self.__name)

totallyNotFrancis = Person("Frank", "M")

totallyNotFrancis.__name = "Francis"

print(totallyNotFrancis)


