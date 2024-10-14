class DatabaseConnectionException(Exception):
    def __init__(self):
        message = "Failed to establish a proper connection to the database"
        super().__init__(message)
