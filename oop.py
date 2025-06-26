class Employee:
    def __init__(self, eid, name, dept, salary):
        self.eid = eid
        self.name = name
        self.dept = dept
        self.salary = salary

    def display(self):
        print(f"{self.eid} | {self.name} | {self.dept} | ₹{self.salary}")


class EmployeeSystem:
    def __init__(self):
        self.emp_list = []

    def add(self, eid, name, dept, salary):
        self.emp_list.append(Employee(eid, name, dept, salary))

    def show_all(self):
        for emp in self.emp_list:
            emp.display()

    def search(self, eid):
        for emp in self.emp_list:
            if emp.eid == eid:
                emp.display()
                return
        print("Not found")
system = EmployeeSystem()
system.add("101", "Anant", "IT", "50000")
system.add("102", "Saksham", "HR", "45000")

system.show_all()
system.search("101")
