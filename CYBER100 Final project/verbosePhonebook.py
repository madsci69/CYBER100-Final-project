#Verbose Phone Book

import csv
import pickle


def loadPhonebook(file):
    try:
        with open (file + ".pkl", 'rb') as f:
            phoneBook = pickle.load(f)
        # with open ("verbosePhonebook.csv", "r") as f:
        #     reader = csv.reader(f)
        #     phoneBook = {rows[0]: rows[1] for rows in reader}
        #     # for rows in reader:
        #     #   phoneBook[rows[0]] = rows[1]
        return phoneBook
    except FileNotFoundError:
        print("That is not a valid file. ")
        phoneBook = {}
        return phoneBook
    except:
        print("You broke it. ")
    #Should add option to load different phone books?

# def makePhonebook(name):
#     with open (name+".pkl", "wb") as j:
#         pickle.dump("", j)


def savePhonebook(phoneDict):
    fileName = input("What do you want to name your phoneBook? ")

    with open (fileName + ".pkl",'wb') as f:
        pickle.dump(phoneDict, f, protocol=pickle.HIGHEST_PROTOCOL)


def printPhonebook(dict):
    for key, value in dict.items():
        print('{} : {}'.format(key, value))

def findNum(name):
    if name in phoneBook:
        number = phoneBook[name]
        print("The phone number for {} is {}. ".format(name, number))
    else:
        print("That name is not in the phonebook. ")

def reversePhoneSearch(number):
    try:
        name = {key for key in phoneBook if phoneBook[key]==int(number)}
        print("The name that corresponds with {} is {}. ".format(number, name))
    except ValueError:
        print("That is not a valid phone number. Please print the number with no spaces or dashes. ")
    except:
        print("You broke it. ")

def addNumber(name, number):
    phoneBook[name] = number

def deleteNumber(name):
    if name in phoneBook:
        print("{} will be deleted from the phonebook. ".format(name))
        phoneBook.pop(name)
    else:
        print("That name is not in the phonebook. ")
    





if __name__ == "__main__":

    print("Welcome to the Verbose Phonebook. ")

    print("Do you want to start a new phonebook, or open an existing one? Press (1) for a new one, or (2) to open an existing phonebook. ")
    loader = input()
    if loader == "2":
        print("What is the name of the phonebook? ")
        resp = input()
        phoneBook = loadPhonebook(resp)
    elif loader == "1":
        phoneBook = {}
    else:
        print("That was not a valid choice. We will load a new phonebook. ")
        phoneBook = {}


    while True:
        print("Choose from the following prompts: ")
        choice = input("""
        1. Print entire phonebook
        2. Find a phone number by name
        3. Reverse search by phone number
        4. Add a phone number
        5. Delete a phone number
        6. Quit the verbose phonebook
        7. Load a different phonebook
        """)
        if choice.isnumeric():

            if int(choice) == 6:
                print("Do you want to save the changes to the verbose phonebook? Y or N?")
                save = input()
                if save.lower() == "y":
                    savePhonebook(phoneBook)
                    quit()
                else:
                    quit()
            elif int(choice) == 1:
                printPhonebook(phoneBook)

            elif int(choice) == 2:
                name = input("What is the name of the contact? ")
                findNum(name)
            
            elif int(choice) == 3:
                number = input("What is the phone number? ")
                reversePhoneSearch(number)

            elif int(choice) == 4:
                name = input("What is the name? ")
                number = input("What is their phone number? ")
                if number.isnumeric():
                    addNumber(name, int(number))
                    printPhonebook(phoneBook)
                else:
                    print("The phone number has to be integers only, with no dashes, spaces, or other symbols. ")

            elif int(choice) == 5:
                name = input("Enter the name to delete from the phonebook: ")
                deleteNumber(name)
                
            else:
                print("That is not a valid choice. Please try again. ")
        else:
            print("That is not a valid choice. ")