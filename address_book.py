class AddressBook():

    def __init__(self):
        self.contact_book= []
        self.user_contact = {}

    def print_contact_book(self):
        for key, value in self.user_contact.items():
            print("{:<20}".format(key),end="")
        print("\n-------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for contact in self.contact_book:
            for key, value in contact.items():
                print("{:<20}".format(value),end="")
            print("\n")
    
    # function to create a contact
    def create_contact(self):
        self.first_name = input("# Enter your first name: ")
        self.last_name = input("# Enter your last name: ")
        self.address = input("# Enter your address: ")
        self.city = input("# Enter your city: ")
        self.state = input("# Enter your state: ")
        self.zipp = input("# Enter your zip code: ")
        self.phone = input("# Enter your phone number: ")
        self.email = input("# Enter your email: ")
        self.user_contact = {"first name":self.first_name,"last name":self.last_name, "address":self.address, "city":self.city, "state": self.state, "zip":self.zipp, "phone":self.phone, "email":self.email}
        
    
    # function to add new contact
    def add_new_contact(self):
        self.ch = "y"
        while self.ch == 'y':
            print(self.ch)
            self.create_contact()
            self.contact_book.append(self.user_contact) # appending new contact to address book
            print("\ncontact Added!!")
            self.ch = input("\nPress Y to add another person's details or press X if you are done: ").lower()
        return self.contact_book

# function to edit a contact
    def edit_contact(self):
        print("\n-------EDIT DETAILS-------\n")
        f_name = input("ENTER THE FIRSt NAME: ")
        l_name = input("ENTER THE LAST NAME: ")
        presen_or_not = 0
        for contact in self.contact_book:
            if contact["first name"] == f_name and contact['last name'] == l_name:
                presen_or_not +=1
        if presen_or_not == 0:
            print("Person not present!")
        else:
            details_to_edited = input("ENTER THE TO BE EDITED: ").split(",")
            for contact in self.contact_book:
                if contact["first name"] == f_name and contact['last name'] == l_name:
                    for x in details_to_edited:
                        contact[x] = input(f"ENTER THE NEW {x}: ")

            print("\nEDITED DETAILS ARE:\n")
            self.print_contact_book()

def main_menu():
    choice = 1
    user = AddressBook() # creating instance of address book class
    while choice != 0:
            print("\n1. CREATE A CONTACT")
            print("2. ADD NEW CONTACT")
            print("3. EDIT NEW CONTACT\n")
            print("0. EXIT\n")
            try:
                choice = int(input("ENTER YOUR OPTION: "))
            except ValueError:
                print("Enter a proper value!")
            except Exception as ex:
                print(ex)
            else:
                match choice:
                    case 1:
                        user.create_contact()
                    case 2:
                        user.add_new_contact()
                    case 3:
                        user.edit_contact()
                    


if __name__ == "__main__":
    main_menu()