# Function to read employee data from a CSV file
def read_employee_data(filename: str) -> None:
  """Reads and prints data from CSV file

  Args:
      filename (str): Target File Name
  """
  fileHandler = open(filename, 'r')
  for index, employeeDetail in enumerate(fileHandler):
    # Skip the first index which contains title
    if index == 0:
      pass
    else:
      Name, Age, Gender, Designation, Department, Salary = employeeDetail.split(";")
      print("Name: ", Name)
      print("Age: ", Age)
      print("Gender: ", Gender)
      print("Designation: ", Designation)
      print("Department: ", Department)
      print("Salary: ", Salary)
    
  fileHandler.close()

read_employee_data("./employee-details.csv")


# Function to save employee records to a CSV file
def save_employee_data(filename: str, employee: dict) -> None:
  """Writes into the CSV file for employee details

  Args:
      filename: Name of the file 
      employee: Employee Detail conatining Name, Age, Gender, Designation, Department, Salary
  """
  fileHandler = open(filename, 'a')
  fileHandler.write(';'.join(str(detail) for detail in employee.values()) + "\n")
  fileHandler.close()

employee = {
  "Name": "Ashwani Goyal",
  "Age": 30,
  "Gender": "Male",
  "Designation": "LC",
  "Department": "Delivery",
  "Salary": 1200000
}

save_employee_data("./employee-details.csv", employee)