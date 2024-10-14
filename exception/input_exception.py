class InvalidInputException(Exception):
    def __init__(self):
        message = "Invalid Input"
        super().__init__(message)
