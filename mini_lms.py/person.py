def validate_string(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value.strip()

def validate_int(value, field):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field} must be a positive integer")
    return value

def validate_email(value):
    if not isinstance(value, str) or "@" not in value or "." not in value:
        raise ValueError("Invalid email format")
    return value.strip()


class Person:
    def __init__(self, other=None, name=None, id=None, age=None, address=None, email=None):
        if isinstance(other, Person):  # Copy constructor
            self._name = other._name
            self._id = other._id
            self._age = other._age
            self._address = other._address
            self._email = other._email
        else:
            self._name = validate_string(name, "Name")
            self._id = validate_int(id, "ID")
            self._age = validate_int(age, "Age")
            self._address = validate_string(address, "Address")
            self._email = validate_email(email)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = validate_string(value, "Name")

    @property
    def id(self):
        return self._id  # read-only

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = validate_int(value, "Age")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = validate_string(value, "Address")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = validate_email(value)

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Age: {self.age}, Email: {self.email}, Address: {self.address})"






