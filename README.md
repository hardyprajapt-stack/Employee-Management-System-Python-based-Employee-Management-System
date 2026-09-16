# project5
Python OOP project : Employee Management System


# 👨‍💼 Employee Management System

A simple **Python-based Employee Management System** built using **Object-Oriented Programming (OOP)** concepts.

This project demonstrates important Python OOP concepts including **Classes, Objects, Encapsulation, Inheritance, Polymorphism, Getters, Setters, Constructors, Destructor, `super()`, `issubclass()`, Lists, and Menu-Driven Programming**.

The system allows users to add **Managers** and **Developers**, store them in a list, display employee information, and check class inheritance relationships.

---

## 📌 Project Overview

The **Employee Management System** is a console-based application that manages different types of employees.

The project uses a base class:

```python
Employee
```

and two derived classes:

```python
Manager
Developer
```

Both `Manager` and `Developer` inherit common employee information and functionality from the `Employee` class.

---

# 🎯 Project Objectives

The main objectives of this project are:

* Understand Object-Oriented Programming
* Create classes and objects
* Implement encapsulation
* Implement inheritance
* Demonstrate polymorphism
* Use constructors
* Use destructors
* Create getters and setters
* Use `super()`
* Store multiple objects in a list
* Check inheritance using `issubclass()`
* Build a menu-driven application
* Practice real-world OOP structure

---

# 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming
* Classes & Objects
* Encapsulation
* Inheritance
* Polymorphism
* Constructors
* Destructor
* Getters & Setters
* Lists
* `super()`
* `issubclass()`
* `while` Loop
* Conditional Statements
* User Input

---

# 📂 Project Structure

```text
Employee-Management-System/
│
├── employee_management.py
└── README.md
```

---

# 🧱 OOP Class Structure

The project follows this class hierarchy:

```text
                 Employee
                 /      \
                /        \
          Manager       Developer
             │              │
        Department    Programming Language
```

### Base Class

```text
Employee
```

### Derived Classes

```text
Manager
Developer
```

---

# 👨‍💼 1. Employee Base Class

The `Employee` class is the main/base class.

```python
class Employee:
```

It stores common employee information:

* Employee ID
* Name
* Age
* Salary

The constructor is:

```python
def __init__(self, employee_id=None, name="", age=0, salary=0.0):
```

---

# 🔐 2. Encapsulation

The project demonstrates encapsulation using double underscores.

Employee ID:

```python
self.__employee_id
```

Salary:

```python
self.__salary
```

These attributes are encapsulated inside the `Employee` class.

The program provides methods to access and modify them.

---

## Getter Methods

### Get Salary

```python
def get_salary(self):
    return self.__salary
```

### Get Employee ID

```python
def get_employee_id(self):
    return self.__employee_id
```

Getters allow the program to retrieve encapsulated values.

---

## Setter Methods

### Set Salary

```python
def set_salary(self, new_salary):
    self.__salary = new_salary
```

### Set Employee ID

```python
def set_employee_id(self, new_id):
    self.__employee_id = new_id
```

Setters allow the program to update encapsulated values.

---

# 🖥️ 3. Display Method

The base `Employee` class contains a `display()` method:

```python
def display(self):
```

It displays:

```text
Employee Info
ID
Name
Age
Salary
```

Example:

```text
[Employee Info]
ID: M101
Name: Rahul
Age: 30
Salary: ₹50000.0
```

---

# 🗑️ 4. Destructor

The project also demonstrates a destructor:

```python
def __del__(self):
    print(f"Employee {self.name} deleted.")
```

The destructor is called when an object is being destroyed.

It displays a message containing the employee's name.

---

# 👔 5. Manager Class

The `Manager` class inherits from `Employee`.

```python
class Manager(Employee):
```

This means a Manager gets the common employee properties and methods from the `Employee` class.

The Manager additionally stores:

```text
Department
```

Constructor:

```python
def __init__(self, employee_id, name, age, salary, department):
```

---

## `super()` in Manager

The Manager constructor uses:

```python
super().__init__(employee_id, name, age, salary)
```

This calls the constructor of the `Employee` class.

Therefore, the common employee information is initialized by the base class.

---

## Manager Display

The Manager overrides the `display()` method:

```python
def display(self):
    super().display()
    print(f"Department: {self.department}")
```

First, it displays the common Employee information and then displays the Manager's department.

---

# 💻 6. Developer Class

The `Developer` class also inherits from `Employee`.

```python
class Developer(Employee):
```

The Developer stores:

```text
Programming Language
```

Constructor:

```python
def __init__(self, employee_id, name, age, salary, programming_language):
```

---

## `super()` in Developer

The Developer constructor uses:

```python
super().__init__(employee_id, name, age, salary)
```

This initializes the common Employee information.

---

## Developer Display

The Developer also overrides `display()`:

```python
def display(self):
    super().display()
    print(f"Programming Language: {self.programming_language}")
```

It first displays common Employee information and then displays the programming language.

---

# 🔄 7. Inheritance

The project demonstrates inheritance:

```text
Employee
   │
   ├── Manager
   │
   └── Developer
```

The derived classes inherit common functionality from `Employee`.

### Common Properties

Both Manager and Developer have:

* Employee ID
* Name
* Age
* Salary
* Salary getter/setter
* Employee ID getter/setter
* Display functionality

### Manager-Specific Property

```text
Department
```

### Developer-Specific Property

```text
Programming Language
```

---

# 🎭 8. Polymorphism

Both `Manager` and `Developer` define their own version of:

```python
display()
```

The program can therefore call:

```python
emp.display()
```

without needing to know whether `emp` is a Manager or Developer.

Example:

```python
for emp in employees:
    emp.display()
```

The appropriate `display()` method is executed according to the object.

---

# 📋 9. Employee List

The program creates an empty list:

```python
employees = []
```

Manager and Developer objects are added to this list:

```python
employees.append(m)
```

and:

```python
employees.append(d)
```

This allows multiple employee objects to be stored together.

---

# 🔎 10. Checking Subclass Type

The program uses Python's:

```python
issubclass()
```

function.

It checks:

```python
issubclass(Manager, Employee)
```

and:

```python
issubclass(Developer, Employee)
```

The output is:

```text
Manager is subclass of Employee: True
Developer is subclass of Employee: True
```

This confirms the inheritance relationship.

---

# 🧭 Main Menu

The application provides a menu-driven interface:

```text
===== Employee Management System =====

1. Add Manager
2. Add Developer
3. Display All Employees
4. Check Subclass Type
5. Exit
```

The program uses a `while True` loop so the user can perform multiple operations.

---

# ➕ Add Manager

When the user selects:

```text
1. Add Manager
```

the program asks for:

* Employee ID
* Name
* Age
* Salary
* Department

Example:

```text
Enter ID: M101
Enter Name: Rahul
Enter Age: 30
Enter Salary: 50000
Enter Department: Finance
```

A Manager object is created:

```python
m = Manager(emp_id, name, age, salary, dept)
```

and stored in the employee list.

---

# 💻 Add Developer

When the user selects:

```text
2. Add Developer
```

the program asks for:

* Employee ID
* Name
* Age
* Salary
* Programming Language

Example:

```text
Enter ID: D101
Enter Name: Amit
Enter Age: 25
Enter Salary: 45000
Enter Programming Language: Python
```

A Developer object is created:

```python
d = Developer(emp_id, name, age, salary, lang)
```

and added to the employee list.

---

# 📖 Display All Employees

When the user selects:

```text
3. Display All Employees
```

the program checks whether the employee list is empty.

If there are employees:

```python
for emp in employees:
    emp.display()
```

Each employee's appropriate display method is called.

---

# 🔄 Program Flow

```text
                  START
                    │
                    ▼
              Create List
              employees=[]
                    │
                    ▼
              Display Menu
                    │
        ┌───────────┼────────────┐
        ▼           ▼            ▼
     Manager     Developer     Display
        │           │            │
        └───────────┼────────────┘
                    │
                    ▼
             Check Subclass
                    │
                    ▼
                 Exit?
                /     \
              No       Yes
              │         │
              └──► Menu ▼
                     END
```

---

# 🧪 Example Run

### Main Menu

```text
===== Employee Management System =====
1. Add Manager
2. Add Developer
3. Display All Employees
4. Check Subclass Type
5. Exit

Enter your choice (1-5):
```

### Adding Manager

```text
Enter ID: M101
Enter Name: Rahul
Enter Age: 30
Enter Salary: 50000
Enter Department: Finance

Manager added successfully.
```

### Adding Developer

```text
Enter ID: D101
Enter Name: Amit
Enter Age: 25
Enter Salary: 45000
Enter Programming Language: Python

Developer added successfully.
```

### Displaying Employees

```text
[Employee Info]
ID: M101
Name: Rahul
Age: 30
Salary: ₹50000.0
Department: Finance

[Employee Info]
ID: D101
Name: Amit
Age: 25
Salary: ₹45000.0
Programming Language: Python
```

### Checking Subclasses

```text
Manager is subclass of Employee: True
Developer is subclass of Employee: True
```

---

# 🧩 OOP Concepts Used

| Concept        | Implementation                      |
| -------------- | ----------------------------------- |
| Class          | `Employee`, `Manager`, `Developer`  |
| Object         | Manager and Developer objects       |
| Encapsulation  | `__employee_id`, `__salary`         |
| Getter         | `get_salary()`, `get_employee_id()` |
| Setter         | `set_salary()`, `set_employee_id()` |
| Inheritance    | Manager/Developer → Employee        |
| Polymorphism   | Overridden `display()`              |
| Constructor    | `__init__()`                        |
| Destructor     | `__del__()`                         |
| `super()`      | Calls Employee constructor/display  |
| `issubclass()` | Checks inheritance                  |
| List           | Stores employee objects             |

---

# 📚 What I Learned From This Project

This project provides practical experience with:

* Python Classes
* Objects
* Constructors
* Destructors
* Encapsulation
* Private Attributes
* Getters
* Setters
* Inheritance
* Method Overriding
* Polymorphism
* `super()`
* `issubclass()`
* Lists of Objects
* Loops
* Conditional Statements
* User Input
* Menu-Driven Applications

---

# 💼 Real-World Connection

The project demonstrates a simplified structure similar to employee-management applications.

For example:

```text
Employee
   │
   ├── Manager
   │      └── Department
   │
   └── Developer
          └── Programming Language
```

Common employee information is maintained in the base class, while specialized information is maintained in derived classes.

This approach helps organize related data and behavior using OOP.

---

# 🚀 How to Run

## Step 1 — Install Python

Check whether Python is installed:

```bash
python --version
```

---

## Step 2 — Save the Code

Save the program as:

```text
employee_management.py
```

---

## Step 3 — Open Terminal

Navigate to the project folder:

```bash
cd path\to\Employee-Management-System
```

---

## Step 4 — Run the Program

```bash
python employee_management.py
```

The Employee Management System menu will appear.

---

# ⚠️ Important Notes

* Age is converted using `int()`.
* Salary is converted using `float()`.
* The program currently does not include input validation for invalid age/salary values.
* Employee records are stored only in the program's `employees` list during execution.
* No database or external file storage is currently used.
* The current menu provides adding, displaying, subclass checking, and exiting.
* Getter and setter methods are implemented in the class, although the main menu does not directly use them.

---

# 🔮 Future Improvements

Possible improvements for a future version:

* Add employee search
* Update employee information
* Delete individual employee
* Search by employee ID
* Add more employee types
* Add input validation
* Store employees in CSV
* Store data in MySQL
* Add employee attendance
* Add department-wise analysis
* Add salary analysis
* Create a GUI
* Connect the project with Pandas and Power BI

---

# 📌 Project Highlights

* 👨‍💼 Employee Management
* 🐍 Python OOP
* 🔐 Encapsulation
* 🧬 Inheritance
* 🎭 Polymorphism
* 🔧 Getters & Setters
* 🏗️ Constructors
* 🗑️ Destructor
* 🔄 Method Overriding
* 📦 Object Lists
* 🔎 `issubclass()`
* 🖥️ Menu-Driven Console Application

---

# 👨‍💻 Author

**Hardik Kumawat**

Data Analytics Learner | Python | SQL | Excel | Power BI

---

## ⭐ Project Purpose

This project was created as a practical Python OOP project to strengthen understanding of **encapsulation, inheritance, polymorphism, classes, objects, constructors, destructors, getters, setters, and menu-driven application development**.
