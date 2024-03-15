# creating address book class
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
    
    # function to create a contact
    def create_contact(self):
        try: 
            user_contact = {"first name":self.first_name,"last name":self.last_name, "address":self.address, "city":self.city, "state": self.state, "zip":self.zip, "phone":self.phone, "email":self.email}
            print("\n**Contact created**")
            print("-----------------------------")
            for key, value in user_contact.items():
                print("{:<20}".format(key),end="")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")
            for key, value in user_contact.items():
                print("{:<20}".format(value),end="")
        except Exception as ex:
            print(ex)


user = AddressBook() # creating instance of address book class
user.create_contact()