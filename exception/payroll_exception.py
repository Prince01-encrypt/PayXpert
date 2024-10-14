class PayrollGenerationException(Exception):
    def __init__(self, payroll_id):
        message = f"Unable to generate payroll: Employee with ID {payroll_id} not found."
        super().__init__(message)

