class Person:
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def print_person(self):
        print('name:', self.__name)
        print('address:', self.__address)
        print('phone:', self.__phone_number)


class Customer(Person):
    def __init__(self, name, address, phone_number, customer_number, B_data):
        Person.__init__(self, name, address, phone_number)

        self.__customer_number = customer_number
        self.__Boolean_data_attribute = B_data

    def print_person(self):
        Person.print_person(self):
        print('Customer Number:', self.__cust_number)
        if self.__on_list:
            print('On mail Yes')
        else:
            print('NO.')
