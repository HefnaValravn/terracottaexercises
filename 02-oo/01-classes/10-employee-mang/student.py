class Employee:
    # Initialize class variables
    company_name = "Dev.boot"
    total_employees = 0

    # Constructor
    def __init__(self, first_name, last_name, id, position, salary):
        Employee.total_employees += 1
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary


    # Getter Method
    def get_name(self):
        return self.first_name + " " + self.last_name