class AddressBook():

    def __init__(self):
        self.contact_book= []
        self.user_contact = {}

# method to print the address book
    def print_contact_book(self):
        for key, value in self.user_contact.items(): # print the heading of the address book
            print("{:<20}".format(key),end="")
        print("\n-------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for contact in self.contact_book:
            for key, value in contact.items():
                print("{:<20}".format(value),end="") # print the contacts
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
        return self.user_contact
    
    # function to add new contact
    def add_new_contact(self):
        self.ch = "y"
        while self.ch == 'y': # loop untill you finish adding new contact
            self.create_contact()
            self.contact_book.append(self.user_contact) # appending new contact to address book
            print("\ncontact Added!!")
            self.ch = input("\nPress Y to add another person's details or press X if you are done: ").lower()
        return self.contact_book
    
    # function to add multiple contacts to the address book 
    def add_multiple_contact(self):
        try:
            num_of_contacts = int(input("Enter the number of contacts you want to add: "))
        except ValueError:
            print("\nInvalid Entry!!")
        else:
            for i in range(1,num_of_contacts+1):
                print("\nENTER THE DETAILS OF PERSON",i)
                self.create_contact() # contact is created 
            print("\n",num_of_contacts,"CONTACT(S) ADDED SUCCESSFULLY!!!")

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

    def delete_contact(self):
        conatct_del_fname = input("Enter the first name of the contact to be deleted: ") # name of the contact to be deleted is takes
        conatct_del_lname = input("Enter the last name of the contact to be deleted: ") # name of the contact to be deleted is takes
        present_or_not = 0
        for contact in self.contact_book:
            if contact["first name"] == conatct_del_fname and contact["last name"] == conatct_del_lname: # checking if the user is present in the contact book or not
                present_or_not +=1
        if present_or_not == 0:
            print("\nContact not found!!")
        else:
            for contact in self.contact_book:
                if conatct_del_fname in contact.values() and conatct_del_lname in contact.values():
                    self.contact_book.remove(contact)
                    print("\nContact Deleted")

def main_menu():
    choice = 1
    user = AddressBook() # creating instance of address book class
    while choice != 0:
            print("\n1. CREATE A CONTACT")
            print("2. ADD NEW CONTACT")
            print("3. ADD MULTIPLE CONTACT")
            print("4. EDIT CONTACT")
            print("5. DELETE CONTACT\n")
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
                        user.add_multiple_contact()
                    case 4:
                        user.edit_contact()
                    case 5:
                        user.delete_contact()


if __name__ == "__main__":
    main_menu()