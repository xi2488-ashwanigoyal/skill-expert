class Employee:
    """
    A class to represent an Employee with basic attributes and methods.

    Attributes:
        name (str): The name of the employee.
        age (int): The age of the employee.
        gender (str): The gender of the employee.
    
    Methods:
        update_information: Update the information of the employee.
    """
    def __init__(self, name: str, age: int, gender: int):
        """
        Initialize an Employee object with the given attributes.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            gender (str): The gender of the employee.
        """
        self.name = name
        self.age = age
        self.gender = gender
    
    def update_information(self, name: str=None, age: int=None, gender: str=None) -> None:
        """
        Update the information of the employee.

        Args:
            name (str, optional): The new name of the employee.
            age (int, optional): The new age of the employee.
            gender (str, optional): The new gender of the employee.
        """
        if name:
            self.name = name
        if age:
            self.age = age
        if gender:
            self.gender = gender


class FullTimeEmployee(Employee):
    """
    A class representing a Full-Time Employee, inheriting from Employee.
    """
    def __init__(self, name: str, age: int, gender: int, salary: float):
        """
        Initialize a FullTimeEmployee object with the given attributes.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            gender (str): The gender of the employee.
            salary (float): The salary of the employee.
        """
        super().__init__(name, age, gender)
        self.salary = salary


class PartTimeEmployee(Employee):
    """
    A class representing a Part-Time Employee, inheriting from Employee.
    """
    def __init__(self, name: str, age: int, gender: int, hourly_rate: float):
        """
        Initialize a PartTimeEmployee object with the given attributes.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            gender (str): The gender of the employee.
            hourly_rate (float): The hourly rate of the employee.
        """
        super().__init__(name, age, gender)
        self.hourly_rate = hourly_rate


class Contractor(Employee):
    """
    A class representing a Contractor, inheriting from Employee.
    """
    def __init__(self, name: str, age: int, gender: int, project_duration: str):
        """
        Initialize a Contractor object with the given attributes.

        Args:
            name (str): The name of the contractor.
            age (int): The age of the contractor.
            gender (str): The gender of the contractor.
            project_duration (str): The duration of the contractor's project.
        """
        super().__init__(name, age, gender)
        self.project_duration = project_duration