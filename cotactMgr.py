import csv

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
            if not self.contactExists(contact.getName()):
                self.contacts.append(contact)
            else:
                return "contact already exists"



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
        contact = self.contactExists(contactName)

        return "contact not found" if contact == False else contact

    def viewAllContacts(self):
        for contact in self.contacts:
            print(contact)

    def readContactFromFile(self):
        with open('contacts.txt' , 'rb') as csvFile :
            contactList = csv.reader(csvFile , delimiter = ' ' , quotechar = '|')

        for row in contactList :
            print(', '.join(row))


    def __repr__(self):
        """
        :return: a serialised version of the contacts data
        """
        contactsStr = ""
        for contact in self.contacts:
            contactsStr += "\n" + contact

        return contactsStr

dataList = [None, None, None, None, None]
questions = ["What's you name", "Are you male or Female", "what number do I call you on",
             "can I have you postal address pls", "one more pls, your email"]

commands = ["exit", "add contact", "remove contact", "find contact", "view saved contacts"]

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
    print( "Type:")

    lth = len(commands)
    idx = 0
    while idx < lth :

        print( str(idx + 1)+ " to " + commands[idx])

        # print( "{} to {}". format(str(idx + 1), commands[idx]))



        idx += 1


    command = input(">> ")

    if(command == "2"):
        length = len(questions)
        i = 0
        while i < length:
            print("\n" + questions[i], "?")
            dataList[i] = input(">>")
            i += 1

        contactList.addContact(Contact(name = dataList[0], dataList[1], dataList[2], dataList[3], dataList[4]))

    elif (command == "3"):
        print("\nWhat's you name")
        name = input(">>")

        print(contactList.removeContact(name))

    elif (command == "4"):
        print("\nWhat's you name")
        name = input(">>")
        print(contactList.find(name))

    elif (command == "5"):
        print(contactList.viewAllContacts())

    elif (command == "1"):
        break

    else:
        print("command not found")




