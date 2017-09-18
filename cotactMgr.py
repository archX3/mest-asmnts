
class ContactManager:

    def __init__(self, name = "", gender ="", phoneNumber = "", postalAddress = "", email = ""):
        self.name = name
        self.gender = gender
        self.phoneNumber = phoneNumber
        self.postalAddress = postalAddress
        self.email = email

    def printAllData(self):
        return self.name, self.gender, self.phoneNumber


# name = input("What's you name\n")
# gender = input("Are you male or Female")
# phoneNumber = input("what number do I call you on")
# postalAddress = input("can I have you postal address pls")
# email = input("one more pls, your email")

newContact = ContactManager("Michael", "jnnsnlksd", "jndsd", "bdnskd", "dkjkjbsd")
# newContact = ContactManager(name, gender, phoneNumber, postalAddress, email)

print(newContact.printAllData()[0], newContact.printAllData()[1], newContact.printAllData()[2], )


