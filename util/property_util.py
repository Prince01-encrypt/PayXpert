from exception.input_exception import InvalidInputException

class PropertyUtil:
    @staticmethod
    def fetch_connection_string():
        try:
            SERVER_NAME = "PRINCE\\SQLEXPRESS"
            DATABASE_NAME = "PayXpert"
            
            connection_string = (
                "Driver={SQL Server};"
                f"Server={SERVER_NAME};"
                f"Database={DATABASE_NAME};"
                "Trusted_Connection=yes;"
            )
            return connection_string
        
        except Exception as error:
            raise InvalidInputException("Failed to obtain database connection details") from error
