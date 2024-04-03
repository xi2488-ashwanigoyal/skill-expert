# Variable and Data Types, Collection Concepts & Modules

import employee;

# Employee information variables
employee_name: str = "John Doe"
employee_age: int = 30
employee_gender: str = "Male"
employee_designation: str = "Software Engineer"
employee_department: str = "Engineering"
employee_salary: float = 60000.00

# List to store multiple employee records
employee_records = [
  {
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "designation": "Software Engineer",
    "department": "Engineering",
    "salary": 60000.00
  },
  {
    "name": "Jane Smith",
    "age": 35,
    "gender":"Female",
    "designation": "HR Manager",
    "department": "Human Resources",
    "salary": 70000.00
  }
]

# Tuple to store immutable employee information
employee_immutable_info = ("EMP001", "2021-05-12")

employee_details = [
  {
    "name": "John",
    "salary": 900000
  },
  {
    "name": "Mathew",
    "salary": 1000000
  },
  {
    "name": "Gabriel",
    "salary": 1050000
  }
]
# Using module to print employee records
employee.print_employee_records(employee_details);

# Using module to calculate employee's incremented salary
employee.calculate_employee_incremented_salary(1600000, 67)

# Using module to keep prompting user for input
employee.keep_prompting_user()