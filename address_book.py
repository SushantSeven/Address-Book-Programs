class AddressBook():

    contact_book= []
    user_contact = {}

# method to print the address book
    def print_contact_book(self):
        for key, value in self.user_contact.items(): # print the heading of the address book
            print("{:<20}".format(key),end="")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
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
    
    # function to add multiple contacts to th address book 
    def add_multiple_contact(self,num_of_contacts):
        self.num_of_ccontacts = num_of_contacts
        for i in range(1,num_of_contacts+1):
            print("\nENTER THE DETAILS OF PERSON",i)
            self.create_contact() # contact is created 
            self.contact_book.append(self.user_contact) # contact is appended to the address book
        print("\n",num_of_contacts,"CONTACT(S) ADDED SUCCESSFULLY!!!")

    def edit_contact(self):
        self.add_new_contact() # add new contact is called
        print("\n-------EDIT DETAILS-------\n")
        name = input("ENTER THE NAME: ") # name of the user is taken
        present_or_not = 0
        for contact in self.contact_book:
            if contact["first name"] == name: # checking if the user is present in the contact book or not
                present_or_not +=1
        if present_or_not == 0:
            print("Person not present!")
        else:
            details_to_edited = input("ENTER THE FIELD TO BE EDITED: ")
            for contact in self.contact_book: # editing the details
                    if contact["first name"] == name:
                        contact[details_to_edited] = input(f"ENTER THE NEW {details_to_edited}: ")

            print("\nEDITED DETAILS ARE:\n")
            self.print_contact_book()

    def delete_contact(self):
        self.add_new_contact() # add new contact method is called
        conatct_del = input("Enter the name of the contact to be deleted: ") # name of the contact to be deleted is takes
        for contact in self.contact_book:
            if conatct_del in contact.values():
                contact.clear()  # contact is deleted if it is present in the address book
                print("After deletion-")
                self.print_contact_book()
                return
            else:
                print("Contact not present")

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
                        num_of_contacts = int(input("Enter the number of contacts you want to add: "))
                        user.add_multiple_contact(num_of_contacts)
                    case 4:
                        user.edit_contact()
                    case 5:
                        user.delete_contact()


if __name__ == "__main__":
    main_menu()