import json

class AddressBook():

    def __init__(self, book_name):
        self.contact_book= []
        # self.user_contact = {}
        self.book_name = book_name
        self.header_list = ["first name","last name","address", "city", "state", "zip", "phone", "email"]

# function to read json file
    def read_contact_book(self):
        with open(f"{self.book_name}.json","r") as f:
            dic_reader = json.load(f)
            self.contact_book = list(dic_reader)

# method to print the address book
    def print_contact_book(self):
        self.read_contact_book()
        print("\n~~~~~~~~~~~~~~~~All Contacts~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        for key in self.header_list: # print the heading of the address book
            print("{:<20}".format(key),end="")
        print("\n-------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for contact in self.contact_book:
            for key, value in contact.items():
                print("{:<20}".format(value),end="") # print the contacts
            print("\n")
    
# function to create a contact
    def create_contact(self):
        already_present = 0
        self.first_name = input("# Enter your first name: ")
        self.last_name = input("# Enter your last name: ")
        for l in self.contact_book:
            if self.first_name == l["first name"] and self.last_name == l["last name"]:
                already_present += 1 
        if already_present == 0:
            self.address = input("# Enter your address: ")
            self.city = input("# Enter your city: ")
            self.state = input("# Enter your state: ")
            self.zipp = input("# Enter your zip code: ")
            self.phone = input("# Enter your phone number: ")
            self.email = input("# Enter your email: ")
            self.user_contact = {"first name":self.first_name,"last name":self.last_name, "address":self.address, "city":self.city, "state": self.state, "zip":self.zipp, "phone":self.phone, "email":self.email}
            self.contact_book.append(self.user_contact) # appending new contact to address book
            # field_name  = ["first name","last name","address","city","state","zip","phone","email"]
            with open(f"{self.book_name}.json", 'w') as f: # saving the details in file line by line
                json.dump(self.contact_book, f)
            print("\ncontact Added!!")
        else:
            print("\nPerson Already exists!!")
    
# function to add new contact
    def add_new_contact(self):
        self.ch = "y"
        while self.ch == 'y': # loop untill you finish adding new contact
            self.create_contact()
            self.ch = input("\nPress Y to add another person's details or press X if you are done: ").lower()
        return self.contact_book
    
# function to add multiple contacts to the address book 
    def add_multiple_contact(self):
        try:
            num_of_contacts = int(input("Enter the number of contacts you want to add: "))
        except ValueError:
            print("\nInvalid Option!!")
        else:
            for i in range(1,num_of_contacts+1):
                print("\nENTER THE DETAILS OF PERSON",i)
                self.create_contact() # contact is created 
            print("\n",num_of_contacts,"CONTACT(S) ADDED SUCCESSFULLY!!!")

# function to edit a contact
    def edit_contact(self):
        self.read_contact_book()
        print("\n-------EDIT DETAILS-------\n")
        f_name = input("ENTER THE FIRST NAME: ") # name of the user is taken
        l_name = input("ENTER THE FIRST NAME: ") # name of the user is taken
        present_or_not = 0
        for contact in self.contact_book:
            if contact["first name"] == f_name and contact["last name"] == l_name: # checking if the user is present in the contact book or not
                present_or_not +=1
        if present_or_not == 0:
            print("Person not present!")
        else:
            details_to_edited = input("ENTER THE FIELD TO BE EDITED: ")
            for i in range(len(self.contact_book)): # editing the details
                    if contact["first name"] == f_name and contact["last name"] == l_name:
                        contact[details_to_edited] = input(f"ENTER THE NEW {details_to_edited}: ")

            print("\nEDITED DETAILS ARE:\n")
            self.print_contact_book()

# functio to delete a contact
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
    
    # function to searh a person by city
    def search_by_city(self):
        city_name = input("Enter the city name: ").lower()
        for key, value in self.user_contact.items(): # print the heading of the address book
                    print("{:<20}".format(key),end="")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
        for contact in self.contact_book:
            if contact['city'].lower() == city_name:
                for key, value in contact.items():
                    print("{:<20}".format(value),end="") # print the contacts
                print("\n")
    
    # function to search a person by state
    def view_by_state(self):
        state_name = input("Enter the state name: ").lower()
        for key, value in self.user_contact.items(): # print the heading of the address book
                    print("{:<20}".format(key),end="")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
        for contact in self.contact_book:
            if contact['state'].lower() == state_name:
                for key, value in contact.items():
                    print("{:<20}".format(value),end="") # print the contacts
                print("\n")
 
# function to count the number of contacts by state 
    def count_by_city(self):
        city_count = 0
        city_name = input("Enter the city name: ").lower()
        for contact in self.contact_book:
            if contact['city'].lower() == city_name:
                city_count += 1
        print(f"\nNumber of contacts staying in {city_name}: {city_count}")

#  function to sort contacts by their name
    def sort_by_name(self):
        self.sorted_contacts = sorted(self.contact_book, key = lambda  item: item['first name'])
        print("\n~~~~~~~~~~~~Sorted Contacts Alphabetically~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        for key, value in self.user_contact.items(): # print the heading of the address book
            print("{:<20}".format(key),end="")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
        for contact in self.sorted_contacts:
            for key, value in contact.items():
                print("{:<20}".format(value),end="") # print the contacts
            print("\n")
        
    #  function to sort contacts by zip code
    def sort_by_zip(self):
        self.sorted_contacts_by_zip = sorted(self.contact_book, key = lambda  item: item['zip'])
        print("\n~~~~~~~~~~~~Sorted Contacts By Zip~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        for key, value in self.user_contact.items(): # print the heading of the address book
            print("{:<20}".format(key),end="")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
        for contact in self.sorted_contacts_by_zip:
            for key, value in contact.items():
                print("{:<20}".format(value),end="") # print the contacts
            print("\n") 

def main_menu():
    choice = 1 # variable to loop main menu
    address_book_list = []
    while choice != 0:
            book_already_present = 0
            choice_2 = 1 # variable to loop address book menu
            print("\n_____MAIN~MENU_____\n")
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
                        for book in address_book_list:
                            if book_name in book.keys():
                                book_already_present += 1
                        if book_already_present > 0:
                                print("\nAddress book already exists")
                        else:
                            with open(f'{book_name}.json','a') as f:
                                print(f"\n{book_name} Address book created\n") # creating a txt file for each addressbook
                            new_book = AddressBook(book_name) # creating instance of create new address book
                            address_book_list.append({book_name:new_book}) # saving it in a list as key value pairs
                    case 2: # case to view existing address books
                        if len(address_book_list)>0:
                                for b in range(len(address_book_list)): # displaying address books
                                    for key in address_book_list[b]:
                                        print(b+1,key)
                                try:
                                    book_choice = int(input("\nChoose an address book: ")) # choosing an address book
                                except ValueError:
                                    print("\nInvalid Option!!")
                                else:
                                    if book_choice>=len(address_book_list)+1 or book_choice<=0:
                                        print("\nInvalid address book")
                                    else:
                                        for key, value in address_book_list[book_choice-1].items(): # seperating ke and value addressbook dictionary
                                            book_choice = key
                                            book_choice_value = value
                                        while choice_2 != 0:
                                            print(f"\n~~~~~~~{book_choice} AddressBook MENU~~~~~~~~")
                                            print("\n1. CREATE NEW CONTACT")
                                            print("2. ADD NEW CONTACT")
                                            print("3. ADD MULTIPLE CONTACT")
                                            print("4. EDIT CONTACT")
                                            print("5. DELETE CONTACT")
                                            print("6. SEARCH BY CITY")
                                            print("7. VIEW BY STATE")
                                            print("8. COUNT BY CITY")
                                            print("9. SORT CONTACTS BY NAME")
                                            print("10. SORT CONTACTS BY ZIP CODE")
                                            print("11. PRINT ADDRESS BOOK")
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
                                                            book_choice_value.add_multiple_contact()
                                                        case 4:
                                                            book_choice_value.edit_contact()
                                                        case 5:
                                                            book_choice_value.delete_contact()
                                                        case 6:
                                                            book_choice_value.search_by_city()
                                                        case 7:
                                                            book_choice_value.view_by_state()
                                                        case 8:
                                                            book_choice_value.count_by_city()
                                                        case 9:
                                                            book_choice_value.sort_by_name()
                                                        case 10:
                                                            book_choice_value.sort_by_zip()
                                                        case 11:
                                                            book_choice_value.print_contact_book()

                        else:
                            print("\nNo Address books found!!") # if no address books are present


if __name__ == "__main__":
    main_menu()