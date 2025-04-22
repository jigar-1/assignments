class Person:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Person(name={self.name})"

class Student(Person):
    STATUS_CHOICES = ['freshman', 'sophomore', 'junior', 'senior']

    def __init__(self, name, address, phone, email, status):
        super().__init__(name, address, phone, email)
        if status not in self.STATUS_CHOICES:
            raise ValueError("Invalid status")
        self.status = status

    def __repr__(self):
        return f"Student(name={self.name}, status={self.status})"

class Employee(Person):
    def __init__(self, name, address, phone, email, office, salary, date_hired):
        super().__init__(name, address, phone, email)
        self.office = office
        self.salary = salary
        self.date_hired = date_hired

    def __repr__(self):
        return f"Employee(name={self.name}, office={self.office})"

class Faculty(Employee):
    def __init__(self, name, address, phone, email, office, salary, date_hired, office_hours, rank):
        super().__init__(name, address, phone, email, office, salary, date_hired)
        self.office_hours = office_hours
        self.rank = rank

    def __repr__(self):
        return f"Faculty(name={self.name}, rank={self.rank})"

class Staff(Employee):
    def __init__(self, name, address, phone, email, office, salary, date_hired, title):
        super().__init__(name, address, phone, email, office, salary, date_hired)
        self.title = title

    def __repr__(self):
        return f"Staff(name={self.name}, title={self.title})"

# Test code
p = Person("John Doe", "123 Main St", "123-456-7890", "john@example.com")
s = Student("Jane Doe", "456 Elm St", "9876543210", "jane@example.com", "senior")
e = Employee("Jim Beam", "789 Oak St", "(123)456-7890", "jim@example.com", "101", 50000, "2020-01-01")
f = Faculty("Jill Hill", "321 Pine St", "3216549870", "jill@example.com", "202", 60000, "2019-01-01", "9-5", "Professor")
st = Staff("Jack Black", "654 Birch St", "654-321-0987", "jack@example.com", "303", 40000, "2018-01-01", "Manager")

print(p)
print(s)
print(e)
print(f)
print(st)