class TaxCalculationException(Exception):
    def __init__(self, tax_id):
        message = f"Employee associated with tax ID {tax_id} could not be located."
        super().__init__(message)
