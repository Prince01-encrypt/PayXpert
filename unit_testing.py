import unittest
from datetime import datetime
from entity.employee import Employee
from dao.employee_service import EmployeeService
from dao.payroll_service import PayrollService
from dao.tax_service import TaxService
from exception.employee_exception import EmployeeNotFoundException
from exception.payroll_exception import PayrollGenerationException


class TestPayrollSystem(unittest.TestCase):
    def setUp(self):
        self.employee_service = EmployeeService()
        self.payroll_service = PayrollService()
        self.tax_service = TaxService()

    def tearDown(self):
        pass

    def test_gross_salary_calculation(self):
        test_employee = Employee(
            1,  # EmployeeID
            "Amit",  
            "Verma",  
            datetime(1985, 11, 15),
            "M",  
            "amit.verma@example.in",  
            "9876543210", 
            "Mumbai",  
            "Senior Engineer",  
            datetime(2021, 5, 1),  
            None  
        )
        employee_id = self.employee_service.add_employee(test_employee)
        self.payroll_service.generate_payroll(employee_id, "2024-05-01", "2024-05-31")
        payroll = self.payroll_service.fetch_payrolls_by_period("2024-05-01", "2024-05-31")
        
        self.assertIsNotNone(payroll)

    def test_net_salary_after_deductions(self):
        test_employee = Employee(
            2,"Priya", "Sharma", 1990-12-20, "F", "priya.sharma@example.in", 9876541234,
            "Delhi", "Lead Developer", 2020-02-15, None
        )
        employee_id = self.employee_service.add_employee(test_employee)

        self.payroll_service.generate_payroll(employee_id, "2024-05-01", "2024-05-31")
        payroll = self.payroll_service.fetch_payrolls_by_period("2024-05-01", "2024-05-31")

        self.assertIsNotNone(payroll)

    def test_tax_calculation_for_high_income(self):
        test_employee = Employee(
            3,"Rahul", "Kapoor", "1978-03-25", "M", "rahul.kapoor@example.in", 9988776655,
            "Bengaluru", "Director", "2019-09-10", None
        )
        employee_id = self.employee_service.add_employee(test_employee)
        self.payroll_service.generate_payroll(3, "2024-05-01", "2024-05-31")
        
        payroll = self.payroll_service.fetch_payrolls_by_period("2024-05-01", "2024-05-31")
        tax = self.tax_service.calculate_tax(3, 2024) 

        self.assertIsNotNone(payroll)
        self.assertGreater(tax, 100000)

    def test_payroll_processing_for_multiple_employees(self):
        test_employees = [
            Employee(7,"Anita", "Nair", "1988-07-10", "F", "anita.nair@example.in", 
                     8888777766, "Kochi", "Project Manager", "2018-01-20", None),
            Employee(8,"Vikas", "Mehta", "1993-06-05", "M", "vikas.mehta@example.in", 
                     9999888877, "Pune", "Software Architect", "2020-03-25", None),
            Employee(9,"Sita", "Singh", "1995-09-15", "F", "sita.singh@example.in", 
                     7777666655, "Chennai", "Data Analyst", "2021-07-01", None)
        ]

        employeeTest = 7

        while (employeeTest < 10):
            self.payroll_service.generate_payroll(employeeTest, "2024-05-01", "2024-05-31")
            employeeTest += 1

        while (employeeTest < 10):
            payroll = self.payroll_service.g("2024-05-01", "2024-05-31")
            self.assertIsNotNone(payroll)

    def test_error_handling_for_invalid_employee_data(self):
        with self.assertRaises(EmployeeNotFoundException):
            invalid_employee = Employee(
                "",  # Missing first name
                "Kumar", "1985-11-15", "M", "invalid@example.in", 
                "9876543210", "Hyderabad", "Senior Engineer", "2021-05-01", None
            )
            self.employee_service.add_employee(invalid_employee)


    if __name__ == "__main__":
        unittest.main()
