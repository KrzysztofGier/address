from faker import Faker

faker = Faker()


class BaseContact:
    def __init__(self, name, surname, phone, email_address):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email_address = email_address

    @property
    def label_length(self):
        return len(self.name + ' ' + self.surname)
    
    @property
    def contact_phone(self):   
        return self.phone

    def contact(self):
        print(
            f"Dialing {self.contact_phone}"
            f" and calling {self.name} {self.surname}"
        )

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.email_address}'


class BusinessContact(BaseContact):
    def __init__(self, company, position, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.work_phone = work_phone

    @property
    def label_length(self):
        return len(self.name + ' ' + self.surname)

    @property
    def contact_phone(self):   
        return self.work_phone

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.work_phone}'


def create_contacts(business_card, number):
    address_book = []
    if business_card == 'BaseContact':
        for contact in range(number):
            contact = BaseContact(
                name = faker.first_name(),
                surname = faker.last_name(),
                phone = faker.phone_number(),
                email_address = faker.email()
            )
            address_book.append(contact)
    elif business_card == 'BusinessContact':
        for contact in range(number):
            contact = BusinessContact(
                name = faker.first_name(),
                surname = faker.last_name(),
                phone = faker.phone_number(),
                email_address = faker.email(),
                company = faker.company(),
                position = faker.job(),
                work_phone = faker.phone_number()
            )
            address_book.append(contact)
    else:
        raise ValueError(
            f"Business Card name: {business_card} "
            f"is neither 'BaseContact' nor 'BusinessContact'")
    return address_book


personal_data = create_contacts('BusinessContact', 10)


def address_book(persons):
    for person in persons:
        print(person)


address_book(personal_data)

personal_data[0].contact()