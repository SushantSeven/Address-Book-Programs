class AddressBook():
    # init method to print the heading
    def __init__(self):
         # take user details as input
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.address = input("Enter your address: ")
        self.city = input("Enter your city: ")
        self.state = input("Enter your state: ")
        self.zip = input("Enter your zip code: ")
        self.phone = input("Enter your phone number: ")
        self.email = input("Enter your email: ")
        self.contact_book= []
        self.user_contact = {}
    
    # function to create a contact
    def create_contact(self):
        try:
            self.user_contact = {"first name":self.first_name,"last name":self.last_name, "address":self.address, "city":self.city, "state": self.state, "zip":self.zip, "phone":self.phone, "email":self.email}
            print("Contact created!")
        except:
            print("Opps!! something went wrong!! please try again in some time.")
    # function to add new contact
    def add_new_contact(self):
        try:
            self.contact_book.append(self.user_contact) # appending new contact to address book
        except Exception as ex:
            print(ex)
        else:
            for key, value in self.user_contact.items():
                print("{:<20}".format(key),end="")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")
            for contact in self.contact_book:
                for key, value in contact.items():
                    print("{:<20}".format(value),end="")
                
def main_menu():
    try:
        choice = int(input("Chose your option: "))
    except ValueError:
        print("Enter a proper value!")
    except Exception as ex:
        print(ex)
    else:
        match choice:
            case 1:
                print("Hello")
                user = AddressBook() # creating instance of address book class
                user.create_contact()
            case 2:
                user = AddressBook() # creating instance of address book class
                user.create_contact()
                user.add_new_contact()


if __name__ == "__main__":
    main_menu()