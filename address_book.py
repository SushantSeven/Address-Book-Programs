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
        self.contact_book= []
        self.user_contact = {}
    
    # function to create a contact
    def create_contact(self):
        self.user_contact = {"first name":self.first_name,"last name":self.last_name, "address":self.address, "city":self.city, "state": self.state, "zip":zip, "phone":self.phone, "email":self.email}
    
    # function to add new contact
    def add_new_contact(self):
        self.contact_book.append(self.user_contact) # appending new contact to address book
        print(self.contact_book)

user = AddressBook() # creating instance of address book class
user.create_contact()
user.add_new_contact()