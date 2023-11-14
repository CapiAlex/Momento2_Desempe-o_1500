class Person:
    def __init__(self, id, name, last_name, email, password):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._email = email
        self._password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def register(self):
        self._id = input("Enter the id: ")
        self._name = input("Enter the name: ")
        self._last_name = input("Enter the last name: ")
        self._email = input("Enter the email: ")
        self._password = input("Enter the password: ")

    def view_record(self):
        print(f"Id: {self._id} Name: {self._name} Last Name: {self._last_name} Email: {self._email}")
