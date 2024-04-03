import Employee

# Create a FullTimeEmployee object
full_time_employee = Employee.FullTimeEmployee("Alice", 30, "Female", 50000.0)
print("Full-Time Employee Details:")
print("Name:", full_time_employee.name)
print("Age:", full_time_employee.age)
print("Gender:", full_time_employee.gender)
print("Salary:", full_time_employee.salary)

# Update the information of the FullTimeEmployee
full_time_employee.update_information(name="Alice Smith", age=31)
print("\nUpdated Full-Time Employee Details:")
print("Name:", full_time_employee.name)
print("Age:", full_time_employee.age)

# Create a PartTimeEmployee object
part_time_employee = Employee.PartTimeEmployee("Bob", 25, "Male", 20.0)
print("\nPart-Time Employee Details:")
print("Name:", part_time_employee.name)
print("Age:", part_time_employee.age)
print("Gender:", part_time_employee.gender)
print("Hourly Rate:", part_time_employee.hourly_rate)

# Create a Contractor object
contractor = Employee.Contractor("Charlie", 35, "Male", "6 months")
print("\nContractor Details:")
print("Name:", contractor.name)
print("Age:", contractor.age)
print("Gender:", contractor.gender)
print("Project Duration:", contractor.project_duration)