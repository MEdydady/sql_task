CREATE TABLE IF NOT EXISTS Employees (
	employee_id SERIAL PRIMARY KEY,
	employee_name VARCHAR(80) UNIQUE NOT NULL,
	department_name VARCHAR(40) NOT NULL,
	chief_id INTEGER references Employees(employee_id) unique NOT NULL
);