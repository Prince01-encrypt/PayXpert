from abc import ABC, abstractmethod
from tabulate import tabulate
from entity.employee import Employee
from util.db_connection import DBConnection
from exception.employee_exception import EmployeeNotFoundException


class EmployeeServiceInterface(ABC):
    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def add_employee(self, employee):
        pass

    @abstractmethod
    def update_employee(self, employee, employee_id):
        pass

    @abstractmethod
    def remove_employee(self, employee_id):
        pass


class EmployeeService(DBConnection, EmployeeServiceInterface):
    def get_employee_by_id(self, employee_id):
        try:
            query = "SELECT * FROM Employee WHERE EmployeeID = ?"
            self.cursor.execute(query, (employee_id,))
            result = [list(row) for row in self.cursor.fetchall()]

            if result:
                columns = [
                    "EmployeeID", "FirstName", "LastName", "DateOfBirth", "Gender",
                    "Email", "PhoneNumber", "Address", "Position", "JoiningDate", "TerminationDate"
                ]
                print(tabulate(result, headers=columns, tablefmt="grid"))
            else:
                raise EmployeeNotFoundException(employee_id)
        except Exception:
            print("An unexpected error occurred while retrieving employee data.")


    def get_all_employees(self):
        try:
            query = "SELECT * FROM Employee"
            self.cursor.execute(query)
            result = [list(row) for row in self.cursor.fetchall()]

            if result:
                columns = [
                    "EmployeeID", "FirstName", "LastName", "DateOfBirth", "Gender", "Email",
                    "PhoneNumber", "Address", "Position", "JoiningDate", "TerminationDate"
                ]
                print(tabulate(result, headers=columns, tablefmt="grid"))
            else:
                raise EmployeeNotFoundException("No employees found.")
        except Exception:
            print("An error occurred while fetching the employees.")


    def add_employee(self, employee: Employee):
        try:
            query = """INSERT INTO Employee 
                       (EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, 
                        Position, JoiningDate, TerminationDate) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            self.cursor.execute(query, (
                employee.get_employee_id(), employee.get_first_name(), employee.get_last_name(), employee.get_date_of_birth(), employee.get_gender(),
                employee.get_email(), employee.get_phone_number(), employee.get_address(), employee.get_position(),
                employee.get_joining_date(), employee.get_termination_date()
            ))
            self.conn.commit()
        except Exception as error:
            print(f"Failed to add new employee: {error}")


    def update_employee(self, employee: Employee, employee_id):
        try:
            query = """UPDATE Employee SET
                       EmployeeID = ?,FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Email = ?, 
                       PhoneNumber = ?, Address = ?, Position = ?, JoiningDate = ?, TerminationDate = ? 
                       WHERE EmployeeID = ?"""
            self.cursor.execute(query, (
                employee_id,employee.get_first_name(), employee.get_last_name(), employee.get_date_of_birth(), employee.get_gender(),
                employee.get_email(), employee.get_phone_number(), employee.get_address(), employee.get_position(),
                employee.get_joining_date(), employee.get_termination_date(), employee_id
            ))
            self.conn.commit()
        except Exception as error:
            print(f"Error updating employee record: {error}")


    def remove_employee(self, employee_id):
        try:
            query = "DELETE FROM Employee WHERE EmployeeID = ?"
            self.cursor.execute(query, (employee_id,))
            self.conn.commit()
        except Exception:
            raise EmployeeNotFoundException(employee_id)
