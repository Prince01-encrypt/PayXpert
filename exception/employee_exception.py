class EmployeeNotFoundException(Exception):
    def __init__(self, employee_id):
        message = f"Unable to locate employee with ID: {employee_id}"
        super().__init__(message)

