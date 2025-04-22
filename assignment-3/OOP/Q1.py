class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name={self.name})"

class Student(Person):
    def __init__(self, name, status):
        super().__init__(name)
        self.status = status

    def __repr__(self):
        return f"Student(name={self.name}, status={self.status})"

class Employee(Person):
    def __init__(self, name, office, salary, date_hired):
        super().__init__(name)
        self.office = office
        self.salary = salary
        self.date_hired = date_hired

    def __repr__(self):
        return f"Employee(name={self.name}, office={self.office})"

class Faculty(Employee):
    def __init__(self, name, office, salary, date_hired, office_hours, rank):
        super().__init__(name, office, salary, date_hired)
        self.office_hours = office_hours
        self.rank = rank

    def __repr__(self):
        return f"Faculty(name={self.name}, rank={self.rank})"

class Staff(Employee):
    def __init__(self, name, office, salary, date_hired, title):
        super().__init__(name, office, salary, date_hired)
        self.title = title

    def __repr__(self):
        return f"Staff(name={self.name}, title={self.title})"

# Create objects
a = Person("Alice")
b = Person("Bob")
c = Student("Charlie", "freshman")
d = Student("David", "sophomore")
e = Student("Eve", "junior")
f = Faculty("Frank", "101", 50000, "2020-01-01", "9-5", "Professor")
g = Faculty("Grace", "102", 60000, "2019-01-01", "10-6", "Associate Professor")
h = Staff("Hank", "201", 40000, "2018-01-01", "Manager")
k = Staff("Ivy", "202", 45000, "2017-01-01", "Assistant Manager")
l = Employee("Jack", "301", 55000, "2021-01-01")
m = Employee("Jill", "302", 56000, "2021-06-01")
n = Employee("John", "303", 57000, "2022-01-01")
o = Employee("Jane", "304", 58000, "2022-06-01")
p = Employee("Joe", "305", 59000, "2023-01-01")

# Store objects in a dictionary
data = {
    'Person': [a, b],
    'Student': [c, d, e],
    'Faculty': [f, g],
    'Staff': [h, k],
    'Employee': [l, m, n, o, p],
}

# Generator functions
def get_students():
    for student in data['Student']:
        yield student

def get_employees():
    for employee in data['Employee']:
        yield employee

def get_faculties():
    for faculty in data['Faculty']:
        yield faculty

def get_staffs():
    for staff in data['Staff']:
        yield staff

# Test generators
print("Students:")
for student in get_students():
    print(student)

print("\nEmployees:")
for employee in get_employees():
    print(employee)

print("\nFaculties:")
for faculty in get_faculties():
    print(faculty)

print("\nStaffs:")
for staff in get_staffs():
    print(staff)