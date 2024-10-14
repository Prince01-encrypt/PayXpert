CREATE DATABASE PayXpert;
USE PayXpert;

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(80),
    LastName VARCHAR(80),
    DateOfBirth DATE,
    Gender VARCHAR(15),
    Email VARCHAR(150),
    PhoneNumber VARCHAR(12),
    Address VARCHAR(225),
    Position VARCHAR(80),
    JoiningDate DATE,
    TerminationDate DATE NULL
);

CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY,
    EmployeeID INT,
    PayPeriodStartDate DATE,
    PayPeriodEndDate DATE,
    BasicSalary DECIMAL(12, 2),
    OvertimePay DECIMAL(12, 2),
    Deductions DECIMAL(12, 2),
    NetSalary DECIMAL(12, 2),
	CONSTRAINT FK_Payroll_Employee FOREIGN KEY (EmployeeID) 
		REFERENCES Employee(EmployeeID)
		ON DELETE CASCADE
);

CREATE TABLE Tax (
    TaxID INT PRIMARY KEY,
    EmployeeID INT,
    TaxYear INT,
    TaxableIncome DECIMAL(12, 2),
    TaxAmount DECIMAL(12, 2),
	CONSTRAINT FK_Tax_Employee FOREIGN KEY (EmployeeID) 
		REFERENCES Employee(EmployeeID)
		ON DELETE CASCADE
);

CREATE TABLE FinancialRecord (
    RecordID INT PRIMARY KEY,
    EmployeeID INT,
    RecordDate DATE,
    Description VARCHAR(225),
    Amount DECIMAL(12, 2),
    RecordType VARCHAR(80),
	CONSTRAINT FK_FinancialRecord_Employee FOREIGN KEY (EmployeeID) 
		REFERENCES Employee(EmployeeID)
		ON DELETE CASCADE
);


INSERT INTO Employee
    (EmployeeID ,FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate)
VALUES
    (1,'Prince', 'Patel', '2001-08-20', 'M', 'prince@example.com', '183686774', 'Jhansi', 'Senior Developer', '2021-01-16', NULL),
    (2,'Raman', 'Singh', '2000-11-09', 'M', 'raman@example.com', '9847543210', 'Kanpur', 'Tester', '2020-09-09', NULL);


INSERT INTO Payroll
    (PayrollID,EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary)
VALUES
    (1,1, '2024-10-10', '2024-10-20', 700000, 30000, 50000, 680000),
    (2,2, '2024-10-10', '2024-10-20', 800000, 30000, 50000, 780000);


INSERT INTO Tax
    (TaxID,EmployeeID, TaxYear, TaxableIncome, TaxAmount)
VALUES
    (1,1, 2024, 700000, 30000),
    (2,2, 2024, 800000, 37000);


INSERT INTO FinancialRecord
    (RecordID,EmployeeID, RecordDate, Description, Amount, RecordType)
VALUES
    (1,1, '2024-10-10', 'Bonus', 5000.00, 'Salary'),
    (2,2, '2024-10-10', 'Award', 6000.00, 'Salary');