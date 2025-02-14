import os

FILE = 'contacts/'
EXTENSION = '.txt'

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

    with open(FILE + contact_name + EXTENSION, 'w') as archive:
        archive.write('Name' + contact_name + '\r\n')

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