 # Base Class: Employee
class Employee:
    def __init__(self, employee_id=None, name="", age=0, salary=0.0):
        self.__employee_id = employee_id  # Encapsulated
        self.name = name
        self.age = age
        self.__salary = salary

    # Encapsulation: Getters and Setters
    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, new_id):
        self.__employee_id = new_id

    # Display method
    def display(self):
        print(f"\n[Employee Info]")
        print(f"ID: {self.__employee_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: ₹{self.__salary}")

    # Destructor
    def __del__(self):
        print(f"Employee {self.name} deleted.")

# Derived Class: Manager
class Manager(Employee):
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

# Derived Class: Developer
class Developer(Employee):
    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")

# Menu-Driven UI
def main():
    employees = []

    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Manager")
        print("2. Add Developer")
        print("3. Display All Employees")
        print("4. Check Subclass Type")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            emp_id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            m = Manager(emp_id, name, age, salary, dept)
            employees.append(m)
            print("Manager added successfully.")

        elif choice == "2":
            emp_id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")
            d = Developer(emp_id, name, age, salary, lang)
            employees.append(d)
            print("Developer added successfully.")

        elif choice == "3":
            if not employees:
                print("No employees to display.")
            for emp in employees:
                emp.display()

        elif choice == "4":
            print("Manager is subclass of Employee:", issubclass(Manager, Employee))
            print("Developer is subclass of Employee:", issubclass(Developer, Employee))

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()  
        