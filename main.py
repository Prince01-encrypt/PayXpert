from dao.employee_service import EmployeeService
from dao.payroll_service import PayrollService
from dao.tax_service import TaxService
from dao.financial_service import FinancialService
from entity.employee import Employee
from entity.financial_record import FinancialRecord
from exception.employee_exception import EmployeeNotFoundException
from exception.input_exception import InvalidInputException

class AppMenu:
    emp_service = EmployeeService()
    payroll_service = PayrollService()
    tax_service = TaxService()
    finance_service = FinancialService()

    def show_employee_menu(self):
        while True:
            print("1. Fetch employee by ID")
            print("2. List all employees")
            print("3. Add a new employee")
            print("4. Modify existing employee")
            print("5. Remove an employee")
            print("6. Return to Main Menu\n")

            option = int(input("Select an option from the menu: "))

            if option == 1:
                emp_id = int(input("Enter Employee ID: "))
                self.emp_service.get_employee_by_id(emp_id)
            elif option == 2:
                self.emp_service.get_all_employees()
            elif option == 3:
                em_id = input("Employee ID: ")
                first = input("First Name: ")
                last = input("Last Name: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                gender = input("Gender: ")
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ")
                role = input("Position: ")
                join_date = input("Joining Date (YYYY-MM-DD): ")
                termination = input("Termination Date (YYYY-MM-DD, if applicable): ")
                
                new_emp = Employee(em_id, first, last, dob, gender, email, phone, address, role, join_date, termination)
                self.emp_service.add_employee(new_emp)
            elif option == 4:
                emp_id = int(input("Employee ID to update: "))
                first = input("First Name: ")
                last = input("Last Name: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                gender = input("Gender: ")
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ")
                role = input("Position: ")
                join_date = input("Joining Date (YYYY-MM-DD): ")
                termination = input("Termination Date (YYYY-MM-DD, if applicable): ")
                
                updated_emp = Employee(emp_id, first, last, dob, gender, email, phone, address, role, join_date, termination)
                self.emp_service.update_employee(updated_emp, emp_id)
            elif option == 5:
                emp_id = int(input("Employee ID to delete: "))
                self.emp_service.remove_employee(emp_id)
            elif option == 6:
                break
            else:
                print("Invalid selection, please try again.")

    def show_payroll_menu(self):
        while True:
            print("1. Create payroll")
            print("2. Retrieve payroll by ID")
            print("3. Get payroll for an employee")
            print("4. Get payroll for a time period")
            print("5. Return to Main Menu\n")

            option = int(input("Select an option: "))

            if option == 1:
                emp_id = int(input("Enter Employee ID: "))
                start = input("Start Date (YYYY-MM-DD): ")
                end = input("End Date (YYYY-MM-DD): ")
                self.payroll_service.generate_payroll(emp_id, start, end)
            elif option == 2:
                payroll_id = int(input("Enter Payroll ID: "))
                self.payroll_service.fetch_payroll_by_id(payroll_id)
            elif option == 3:
                emp_id = int(input("Enter Employee ID: "))
                self.payroll_service.fetch_payrolls_by_employee(emp_id)
            elif option == 4:
                start = input("Start Date (YYYY-MM-DD): ")
                end = input("End Date (YYYY-MM-DD): ")
                self.payroll_service.fetch_payrolls_by_period(start, end)
            elif option == 5:
                break
            else:
                print("Invalid option, please try again.")

    def show_tax_menu(self):
        while True:
            print("1. Compute tax")
            print("2. Fetch tax by ID")
            print("3. Retrieve taxes for an employee")
            print("4. View taxes for a year")
            print("5. Return to Main Menu")

            option = int(input("Select an option: "))

            if option == 1:
                emp_id = int(input("Employee ID: "))
                year = input("Tax Year: ")
                result = self.tax_service.calculate_tax(emp_id, year)
                print(f"Total Tax: {result} rupees\n")
            elif option == 2:
                tax_id = int(input("Tax ID: "))
                result = self.tax_service.get_tax_by_id(tax_id)
                print(result)
            elif option == 3:
                emp_id = int(input("Employee ID: "))
                result = self.tax_service.get_tax_for_employee(emp_id)
                print(result)
            elif option == 4:
                year = input("Tax Year: ")
                rows = self.tax_service.get_tax_for_year(year)
                if rows:
                    for row in rows:
                        print(row)
            elif option == 5:
                break
            else:
                print("Invalid choice, please try again.")

    def show_financial_record_menu(self):
        while True:
            print("1. Add a new financial record")
            print("2. Fetch record by ID")
            print("3. Retrieve financial records for an employee")
            print("4. Get financial records for a specific date")
            print("5. Return to Main Menu\n")

            option = int(input("Choose an option: "))

            if option == 1:
                rec_id = input("Record ID: ")
                employee_id = input("Employee ID: ")
                rec_date = input("DATE (YYYY-MM-DD): ")
                des = input("Description: ")
                amount = input("Amount: ")
                rec_type = input("Record Type: ")

                new_rec = FinancialRecord(rec_id, employee_id, rec_date, des, amount, rec_type)
                self.finance_service.add_financial_record(new_rec)
            elif option == 2:
                record_id = int(input("Record ID: "))
                result = self.finance_service.retrieve_financial_record_by_id(record_id)
                print(result)
            elif option == 3:
                emp_id = int(input("Employee ID: "))
                result = self.finance_service.retrieve_financial_records_by_employee(emp_id)
                print(result)
            elif option == 4:
                date_record = input("Record Date: ")
                rows = self.finance_service.retrieve_financial_records_by_date(date_record)
                if rows:
                    for row in rows:
                        print(row)
            elif option == 5:
                break
            else:
                print("Invalid selection, please try again.")


def main():
    menu = AppMenu()
    while True:
        print("===== Welcome to PayXpert =====")
        print("\nMain Menu:")
        print("1. Employee Management")
        print("2. Payroll Management")
        print("3. Tax Management")
        print("4. Financial Record Management")
        print("5. Exit the system\n")

        option = int(input("Select an option: "))

        if option == 1:
            menu.show_employee_menu()
        elif option == 2:
            menu.show_payroll_menu()
        elif option == 3:
            menu.show_tax_menu()
        elif option == 4:
            menu.show_financial_record_menu()
        elif option == 5:
            menu.emp_service.close()
            menu.payroll_service.close()
            menu.tax_service.close()
            menu.finance_service.close()
            print("Thanks for using our services.")
            break


if __name__ == "__main__":
    main()
