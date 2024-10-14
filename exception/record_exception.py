class FinancialRecordException(Exception):
    def __init__(self):
        message = "Unable to retrieve the record because it was not found."
        super().__init__(message)
