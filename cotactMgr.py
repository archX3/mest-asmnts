class Contact:
    def __init__(self, name = "", gender ="", phoneNumber = "", postalAddress = "", email = ""):
        self.__name = name
        self.__gender = gender
        self.__phoneNumber = phoneNumber
        self.__postalAddress = postalAddress
        self.__email = email

    def getName(self):
        return self.__name

    def __repr__(self):
        return "name : {}, gender : {}, phone : {}, addr : {}".format(self.__name, self.__gender,
                                                                      self.__phoneNumber, self.__postalAddress)

class ContactManager:
    def __init__(self, contacts = []):
        self.contacts = contacts

    def contactExists(self, contactName):
        for contact in self.contacts:
            if(contact.getName() == contactName):
                return contact
        return False

    def isEmpty(self):
        return len(self.contacts) == 0

    def addContact(self, contact):
        if self.isEmpty():
            self.contacts.append(contact)
        else:
            if not self.contactExists(contact):
                self.contacts.append(contact)

    def removeContact(self, contactName):
        if self.isEmpty():
            return "cannot remove from an empty list"
        else:

            contact = self.contactExists(contactName)

            if contact:
                self.contacts.remove(contact)
                return contact
            else:
                return "contact not found"

    def find(self, contactName):
        return self.contactExists(contactName)

    def viewAllContacts(self):
        for contact in self.contacts:
            print(contact)



    def __repr__(self):
        return ""

dataList = []

# name = input("What's you name\n")
# gender = input("Are you male or Female")
# phoneNumber = input("what number do I call you on")
# postalAddress = input("can I have you postal address pls")
# email = input("one more pls, your email")

contactList = ContactManager()

# contactList.addContact(Contact("nana", "M", "+233 49 38920 3", "idk", "abc.efg.xyz"))
# contactList.addContact(Contact("ama", "M", "+233 49 38920 3", "idk", "abc.efg.xyz"))
# contactList.addContact(Contact("kwesi", "M", "+233 49 38920 3", "idk", "abc.efg.xyz"))

# print(contactList.find("nana"))
# print(contactList.viewAllContacts())

# print(contactList.removeContact("ahmad"))
# newContact = ContactManager(name, gender, phoneNumber, postalAddress, email)

# print(newContact.printAllData()[0], newContact.printAllData()[1], newContact.printAllData()[2], )

while True:
    print( "Type 1 to exit loop, 2 to add contact, 3 to remove contact, 4 to find contact")
    command = input("> ")

    if(command == "2"):

        name = input("What's you name\n")
        gender = input("Are you male or Female")
        phoneNumber = input("what number do I call you on")
        postalAddress = input("can I have you postal address pls")
        email = input("one more pls, your email")

        contactList.addContact(Contact(name , gender , phoneNumber , postalAddress , email))

    elif (command == "3"):
        name = input("What's you name\n")
        print(contactList.removeContact(name))

    elif (command == "4"):
        name = input("What's you name\n")
        print(contactList.find("nana"))




