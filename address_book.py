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
    
# function to add multiple contacts to the address book 
    def add_multiple_contact(self,num_of_contacts):
        self.num_of_ccontacts = num_of_contacts
        for i in range(1,num_of_contacts+1):
            print("\nENTER THE DETAILS OF PERSON",i)
            self.create_contact() # contact is created 
            self.contact_book.append(self.user_contact) # contact is appended to the address book
        print("\n",num_of_contacts,"CONTACT(S) ADDED SUCCESSFULLY!!!")

# function to edit a contact
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

# functio to delete a contact
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

# class to create a new address book
class CreateAddressBook(AddressBook):
        def create_contact(self):
            super().create_contact()
        def add_new_contact(self):
            super().add_new_contact()
        def add_multiple_contact(self):
            super().add_multiple_contact(num_of_contacts=2)
        def edit_contact(self):
            super().edit_contact()
        def deleted_contact(self):
            super().delete_contact()

def main_menu():
    choice = 1 # variable to loop main menu
    choice_2 = 1 # variable to loop address book menu
    address_book_list = []
    while choice != 0:
            print("\n_____MAIN---MENU_____\n")
            print("1. CREATE AN ADDRESS BOOK")
            print("2. SELECT ADDRESS BOOK")
            try:
                choice = int(input("ENTER YOUR OPTION: "))
                if choice != 1 and choice != 2: # checking if the selected opton exists or not
                    print("\nInvalid Choice!!")
            except ValueError:
                print("\nPlease select a valid option!!")
            except Exception as ex:
                print(ex)
            else: # move to else if the selected option exits
                match choice:
                    case 1: # case to create a new address book
                        book_name = input("\nENTER THE ADDRESS BOOK NAME: ") # enter the address book name
                        if book_name in address_book_list:
                            print("\nAddress book already present")
                        else:
                            new_book = CreateAddressBook() # creating instance of create new address book
                            address_book_list.append({book_name:new_book}) # saving it in a list as key value pairs
                    case 2: # case to view existing address books
                        if len(address_book_list)>0:
                                for b in range(len(address_book_list)): # displaying address books
                                    for key in address_book_list[b]:
                                        print(b+1,key)
                                book_choice = int(input("\nChoose an address book: ")) # choosing an address book
                                if book_choice>=len(address_book_list)+1 or book_choice<=0:
                                    print("\nInvalid address book")
                                else:
                                    for key, value in address_book_list[book_choice-1].items(): # seperating ke and value addressbook dictionary
                                        book_choice = key
                                        book_choice_value = value 
                                    while choice_2 != 0:
                                        print(f"---{book_choice} AddressBook MENU---")
                                        print("\n1. CREATE NEW CONTACT")
                                        print("2. ADD NEW CONTACT")
                                        print("3. ADD MULTIPLE CONTACT")
                                        print("4. EDIT CONTACT")
                                        print("5. DELETE CONTACT")
                                        print("0. GO BACK TO MAIN MENU\n")
                                        try:
                                            choice_2 = int(input("\nEnter your option: "))
                                        except ValueError:
                                            print("\nInvalid option")
                                        except Exception as ex:
                                            print(ex)
                                        else:
                                            match choice_2:
                                                    case 1:
                                                        book_choice_value.create_contact()
                                                    case 2:
                                                        book_choice_value.add_new_contact()
                                                    case 3:
                                                        num_of_contacts = int(input("Enter the number of contacts you want to add: "))
                                                        book_choice_value.add_multiple_contact(num_of_contacts)
                                                    case 4:
                                                        book_choice_value.edit_contact()
                                                    case 5:
                                                        book_choice_value.delete_contact()
                        else:
                            print("\nNo Address books found!!") # if no address books are present


if __name__ == "__main__":
    main_menu()