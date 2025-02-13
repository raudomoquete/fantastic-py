import os

FILE = 'contacts/'

def app():
    # Ensure if the file exist or not
    create_directory()

def create_directory():
    if not os.path.exists(FILE):
        #create file
        os.makedirs(FILE)

    app()