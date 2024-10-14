from abc import ABC, abstractmethod
from tabulate import tabulate
from util.db_connection import DBConnection
from exception.payroll_exception import PayrollGenerationException


class PayrollServiceInterface(ABC):
    @abstractmethod
    def generate_payroll(self, Payroll):
        pass

    @abstractmethod
    def fetch_payroll_by_id(self, payroll_id):
        pass

    @abstractmethod
    def fetch_payrolls_by_employee(self, Payroll):
        pass

    @abstractmethod
    def fetch_payrolls_by_period(self, Payroll):
        pass


class PayrollService(DBConnection, PayrollServiceInterface):
    def generate_payroll(self, employee_id, start_date, end_date):
        try:
            query = """SELECT * 
                       FROM PayRoll 
                       WHERE EmployeeID = ? AND PayPeriodStartDate = ? AND PayPeriodEndDate = ?"""
            self.cursor.execute(query, (employee_id, start_date, end_date))
            payroll_data = self.cursor.fetchall()
            
            if payroll_data:
                print(tabulate(payroll_data))
            else:
                raise PayrollGenerationException(employee_id)
                
        except Exception as error:
            print(f"Error occurred during payroll generation: {error}")
  

    def fetch_payroll_by_id(self, payroll_id):
        try:
            query = "SELECT * FROM PayRoll WHERE PayrollID = ?"
            self.cursor.execute(query, (payroll_id,))
            payroll_record = self.cursor.fetchall()
            print(tabulate(payroll_record))
            self.conn.commit()
            
        except Exception as error:
            print(f"Failed to retrieve payroll by ID: {error}")


    def fetch_payrolls_by_employee(self, employee_id):
        try:
            query = "SELECT * FROM PayRoll WHERE EmployeeID = ?"
            self.cursor.execute(query, (employee_id,))
            payroll_records = self.cursor.fetchall()
            print(tabulate(payroll_records))
            self.conn.commit()
            
        except Exception as error:
            print(f"Failed to retrieve payrolls for employee: {error}")


    def fetch_payrolls_by_period(self, start_date, end_date):
        try:
            query = """SELECT * 
                       FROM PayRoll 
                       WHERE PayPeriodStartDate = ? AND PayPeriodEndDate = ?"""
            self.cursor.execute(query, (start_date, end_date))
            payroll_records = self.cursor.fetchall()
            print(tabulate(payroll_records))
            self.conn.commit()
            
        except Exception as error:
            print(f"Failed to retrieve payrolls for the specified period: {error}")
        
        return payroll_records
    
    
    def calculate_gross_salary(self, employee_id):
        try:
            query = """SELECT BasicSalary, OvertimePay 
                       FROM PayRoll 
                       WHERE EmployeeID = ?"""
            self.cursor.execute(query, (employee_id,))
            payroll_record = self.cursor.fetchone()
            
            if payroll_record:
                basic_salary, overtime_pay = payroll_record
                gross_salary = basic_salary + overtime_pay
                return gross_salary
            else:
                raise PayrollGenerationException(employee_id)

        except Exception as error:
            print(f"Error occurred while calculating gross salary: {error}")
            return None
