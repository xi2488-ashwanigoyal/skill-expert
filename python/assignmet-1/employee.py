# For loop example
def print_employee_records(employee_records: dict):
  """Prints Employee Record on console

  Args:
      employee_records (dict): Employee Dictionary containing name and salary
  """
  for record in employee_records:
      print("Name: ", record["name"])
      print("Salary: ₹", record["salary"], "\n")

# If-else statement example
def calculate_employee_incremented_salary(salary, performance_score):
  if performance_score >= 80:
      salary *= 1.1  # 10% salary increment for high performance
  elif performance_score >= 60:
      salary *= 1.05  # 5% salary increment for average performance

  print("Incremented Salary turns to be: ₹", salary)


# While loop example
def keep_prompting_user():
  """To keep asking for user input until 'quit' is provided as input
  """
  user_input = ""

  # Continue prompting the user until they enter "quit"
  while user_input.lower() != "quit":
      user_input = input("Please enter something (type 'quit' to exit): ")
      print("You entered:", user_input)

  print("Good Bye...")