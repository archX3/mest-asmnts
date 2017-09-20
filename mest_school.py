import random

EIT = "eit"
FELLOW = "fellow"

class Person :
    def __init__(self, name, nationality) :
        self.__name = name
        self.__nationality = nationality

        def get_name(self) :
            return self.__name


class Fellow(Person) :
    def __init__(self, name, nationality, happiness_level = 0) :
        Person.__init__(self, name, nationality)
        self.__happiness_level = happiness_level

    def get_happiness_level(self) :
        return self.__happiness_level

    def set_happiness_level(self, happiness_level) :
        self.__happiness_level = happiness_level

    def eat(self, amount_of_php = 1) :
        self.__happiness_level += amount_of_php

    def teach(self) :
        self.__happiness_level -= 1


class Eit(Person) :
    def __init__(self, name, nationality) :
        Person.__init__(self, name, nationality)
        self.__name = name
        self.__nationality = nationality

    def recite_fun_fact(self, fun_facts) :
        # TODO return a random fun_facts list
        pass


# TODO finish this later
class MestSchool :
    def __init__(self) :
        self.__eits = []
        self.__fellows = []
        self.__tech_class_fun_facts = ["nothing is fun",
                                       "in mest we always give fun facts",
                                       "Andrew hates PHP",
                                       "Francis is rocking N'jiri's hat, well,... not exactly",
                                       "PEP 8 S.U.C.K.S, like for real"]

    def person_exists(self, name, type = EIT) :
        people = self.__eits if type == EIT else self.__fellows
        for person in people :

            if (person.get_name() == name) :
                return person
        return False

    def is_empty(self, type = EIT) :
        """
        :param self:
        :param type: string
        :return:
        """
        return (len(self.__eits) == 0) if (type == EIT) else (len(self.__fellows) == 0)

    def add_person(self, person, type = EIT) :
        people = self.__eits if type == EIT else self.__fellows
        if self.is_empty(type) :
            people.append(person)

        else :
            if not self.person_exists(person.get_name()) :
                people.append(person)
            else :
                return "contact already exists"

    def remove_person(self, person_name, type = EIT) :
        people = self.__eits if type == EIT else self.__fellows
        if self.is_empty(type) :
            return "cannot remove from an empty list"
        else :
            person = self.person_exists(person_name)

            if person :
                people.remove(person)
                return person
            else :
                return "eit not found" if type == EIT else "fellow not found"

    def find(self, person_name, type = EIT):
        person = self.person_exists(person_name, type)

        return "person not found" if person == False else person

    def feed_fellow(self, fellow_name):
        fellow = self.person_exists(fellow_name, FELLOW)

        return "fellow not found" if fellow == False else fellow.eat()



    def get_person(self, items) :
        pass

    def get_fellow(self, name) :
        pass
        # later
