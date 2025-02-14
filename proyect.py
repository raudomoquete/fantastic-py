import os

FILE = 'contacts/'
EXTENSION = '.txt'

#contacts
class Contact:
    def __init__(self, name, phone, category):
        self.name = name
        self.phone = phone
        self.category = category

def app():
    # Ensure if the file exist or not
    create_directory()
    # shows options menu
    show_menu()

    ask = True
    while ask:
        option = input('Select and option: \r\n')
        option = int(option)

        # execute option
        if option == 1:
            add_contact()
            ask = False
        elif option == 2:
            print('Edit Contact')
            ask = False
        elif option == 3:
            print('Show Contact')
            ask = False
        elif option == 4:
            print('Find Contact')
            ask = False
        elif option == 5:
            print('Delete Contact')
            ask = False
        else:
            print('Invalid selection, tray again')

def add_contact():
    print('Write the contact data')
    contact_name = input('Contact Name:\r\n')

    # ensure that contact exist
    exist = os.path.isfile(FILE + contact_name + EXTENSION)

    if not exist:

        with open(FILE + contact_name + EXTENSION, 'w') as archive:
            # fields
            contact_phone = input('add phone number:\r\n')
            contact_category = input('add category:\r\n')

            #class instance
            contact = Contact(contact_name, contact_phone, contact_category)

            #write in the archive
            archive.write('Name' + contact.name + '\r\n')
            archive.write('Phone' + contact.phone + '\r\n')
            archive.write('Category' + contact.category + '\r\n')

            #show success message
            print('\r\r Contact successfully created  \r\n')
    else:
        print('Contact already exist')


def show_menu():
    print('select from menu what you wnat to do:')
    print('1) Add Contact')
    print('2) Edit Contact')
    print('3) Show Contact')
    print('4) Find Contact')
    print('5) Delete Contact')

def create_directory():
    if not os.path.exists(FILE):
        #create file
        os.makedirs(FILE)

if __name__ == '__main__':
    app()