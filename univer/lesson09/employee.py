class Employee:
    def __init__(self, second_name, first_name, email):
        self.second_name = second_name
        self.first_name = first_name
        self.email = email
    def __str__(self):
        return f"{self.second_name};{self.first_name};{self.email}"
