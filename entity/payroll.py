class Payroll:
    def __init__(self, payroll_id, employee_id, start_date, end_date, basic_salary, overtime_pay, deductions, net_salary):
        self.__payroll_id = payroll_id
        self.__employee_id = employee_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__basic_salary = basic_salary
        self.__overtime_pay = overtime_pay
        self.__deductions = deductions
        self.__net_salary = net_salary

    # Getters
    def get_payroll_id(self):
        return self.__payroll_id

    def get_employee_id(self):
        return self.__employee_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_basic_salary(self):
        return self.__basic_salary

    def get_overtime_pay(self):
        return self.__overtime_pay

    def get_deductions(self):
        return self.__deductions

    def get_net_salary(self):
        return self.__net_salary

    # Setters
    def set_payroll_id(self, payroll_id):
        self.__payroll_id = payroll_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_basic_salary(self, basic_salary):
        self.__basic_salary = basic_salary

    def set_overtime_pay(self, overtime_pay):
        self.__overtime_pay = overtime_pay

    def set_deductions(self, deductions):
        self.__deductions = deductions

    def calculate_net_salary(self):
        return self.__basic_salary + self.__overtime_pay - self.__deductions

    # __str__ method for string representation
    def __str__(self):
        return (f"Payroll[ID={self.__payroll_id}, EmployeeID={self.__employee_id}, Period={self.__start_date} to {self.__end_date}, "
                f"BasicSalary={self.__basic_salary}, OvertimePay={self.__overtime_pay}, Deductions={self.__deductions}, NetSalary={self.__net_salary}]")