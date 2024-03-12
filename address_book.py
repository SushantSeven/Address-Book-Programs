# creating address book class
class AddressBook():
    # init method to print the heading
    def __init__(self):
         # take user details as input
        self.first_name = input("Enter your first name: ")
        self.address = input("Enter your address: ")
        self.last_name = input("Enter your last name: ")
        self.city = input("Enter your city: ")
        self.state = input("Enter your state: ")
        self.zip = input("Enter your zip code: ")
        self.phone = input("Enter your phone number: ")
        self.email = input("Enter your email: ")
    
    # function to create a contact
    def create_contact(self):
        user_contact = {"first name":self.first_name,"last name":self.last_name, "address":self.address, "city":self.city, "state": self.state, "zip":zip, "phone":self.phone, "email":self.email}
        print(user_contact)


user = AddressBook() # creating instance of address book class
user.create_contact()