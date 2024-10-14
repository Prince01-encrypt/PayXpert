from abc import ABC, abstractmethod
from entity.tax import Tax
from util.db_connection import DBConnection
from exception.tax_exception import TaxCalculationException


class TaxServiceInterface(ABC):
    @abstractmethod
    def calculate_tax(self, Tax):
        pass

    @abstractmethod
    def get_tax_by_id(self, tax_id):
        pass

    @abstractmethod
    def get_tax_for_employee(self, Tax):
        pass

    @abstractmethod
    def get_tax_for_year(self, Tax):
        pass


class TaxService(DBConnection, TaxServiceInterface):
    def calculate_tax(self, employee_id, tax_year):
        try:
            tax_rate = 0.35
            self.cursor.execute(
                "SELECT TaxableIncome FROM Tax WHERE EmployeeID=? AND TaxYear=?",
                (employee_id, tax_year),
            )
            taxable_income = self.cursor.fetchone()
            if taxable_income:
                tax_amount = float(taxable_income[0]) * tax_rate
                return tax_amount
            else:
                raise TaxCalculationException(f"No tax record found for employee {employee_id}")
        except Exception as e:
            print(f"Error calculating tax: {e}")


    def get_tax_by_id(self, tax_id):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE TaxID=?", (tax_id,))
            row = self.cursor.fetchone()
            if row:
                tax = Tax(row[0], row[1], row[2], row[3], row[4])
                return tax   
            else:
                raise TaxCalculationException(f"No tax data available for Tax ID {tax_id}")
        except Exception as e:
            print(f"Error retrieving tax by ID: {e}")


    def get_tax_for_employee(self, employee_id):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE EmployeeID=?", (employee_id,))
            row = self.cursor.fetchone()
            if row:
                tax = Tax(row[0], row[1], row[2], row[3], row[4])
                return tax 
            else:
                raise TaxCalculationException(f"No tax data found for employee ID {employee_id}")
        except Exception as e:
            print(f"Error fetching tax for employee: {e}")


    def get_tax_for_year(self, tax_year):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE TaxYear=?", (tax_year,))
            rows = self.cursor.fetchall()
            taxes = []
            for row in rows:
                tax = Tax(row[0], row[1], row[2], row[3], row[4])
                taxes.append(tax)
            return taxes
    
        except Exception as e:
            print(f"Error retrieving tax for year {tax_year}: {e}")
