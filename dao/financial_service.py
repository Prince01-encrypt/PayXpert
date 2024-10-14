from abc import ABC, abstractmethod
from entity.financial_record import FinancialRecord
from util.db_connection import DBConnection
from exception.record_exception import FinancialRecordException

class FinancialServiceInterface(ABC):
    @abstractmethod
    def add_financial_record(self, FinancialRecord):
        pass

    @abstractmethod
    def retrieve_financial_record_by_id(self, record_id):
        pass

    @abstractmethod
    def retrieve_financial_records_by_employee(self, FinancialRecord):
        pass

    @abstractmethod
    def retrieve_financial_records_by_date(self, FinancialRecord):
        pass


class FinancialService(DBConnection, FinancialServiceInterface):
    def add_financial_record(self, record: FinancialRecord):
        try:
            query = """INSERT INTO FinancialRecord(RecordID, EmployeeID, RecordDate, Description, Amount, RecordType)
                    VALUES (?, ?, ?, ?, ?, ?)"""
            self.cursor.execute(query, (record.get_record_id(),record.get_employee_id(),record.get_record_date(),record.get_description(), record.get_amount(), record.get_record_type()))
            self.conn.commit()
            
        except Exception as error:
            print("Error during insert operation:", error)


    def retrieve_financial_record_by_id(self, record_id):
        try:
            self.cursor.execute("SELECT * FROM FinancialRecord WHERE RecordID=?", (record_id,))
            row = self.cursor.fetchone()
            if row:
                rec = FinancialRecord(row[0], row[1], row[2], row[3], row[4], row[5])
                return rec 
            else:
                raise FinancialRecordException("Record not found")
        
        except Exception as error:
            print("Error fetching by record ID:", error)


    def retrieve_financial_records_by_employee(self, employee_id):
        try:
            self.cursor.execute("SELECT * FROM FinancialRecord WHERE EmployeeID=?", (employee_id,))
            row = self.cursor.fetchone()
            if row:
                rec = FinancialRecord(row[0], row[1], row[2], row[3], row[4], row[5])
                return rec 
        except Exception as error:
            print("Error fetching by employee ID:", error)


    def retrieve_financial_records_by_date(self, record_date):
        try:
            self.cursor.execute("SELECT * FROM FinancialRecord WHERE RecordDate=?", (record_date,))
            rows = self.cursor.fetchall()
            recs = []
            for row in rows:
                rec = FinancialRecord(row[0], row[1], row[2], row[3], row[4], row[5])
                recs.append(rec)
            return recs
        
        except Exception as error:
            print("Error fetching by date:", error)



