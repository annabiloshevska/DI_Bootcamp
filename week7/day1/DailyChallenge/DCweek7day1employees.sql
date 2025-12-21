CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);
INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

SELECT * FROM employees

-- Identify and handle any missing value.
SELECT *
	FROM employees
	WHERE employee_name IS NULL
	OR salary IS NULL
	OR hire_date IS NULL
	OR department IS NULL

UPDATE employees
SET department = ('Unknown')
WHERE department IS NULL;
--or 
DELETE FROM employees
WHERE department IS NULL;	

-- Check for and eliminate any duplicate rows in the dataset.
SELECT employee_id, COUNT(*) AS duplicate_count
FROM employees
GROUP BY employee_id
HAVING COUNT(*) > 1;

SELECT employee_name, hire_date, salary, department, COUNT(*) AS duplicate_count
FROM employees
GROUP BY employee_name, hire_date, salary, department
HAVING COUNT(*) > 1;

DELETE FROM employees
WHERE ctid NOT IN (
    SELECT MIN(ctid)
    FROM employees
    GROUP BY employee_id
);

-- Correct any structural issues, such as inconsistent naming conventions or formatting errors.

UPDATE employees
SET employee_name = TRIM(employee_name),
    department = TRIM(department);
	
UPDATE employees
SET employee_name = INITCAP(employee_name)
WHERE employee_name ~ '^[a-z]';

SELECT DISTINCT employee_name
FROM employees
ORDER BY employee_name;

SELECT DISTINCT department
FROM employees
ORDER BY department;

-- Ensure all columns have appropriate data types (e.g. the hire_date column).

SELECT hire_date, pg_typeof(hire_date) AS current_type
FROM employees
LIMIT 5;

ALTER TABLE employees ADD COLUMN hire_date_new DATE;

UPDATE employees
SET hire_date_new = TO_DATE(hire_date, 'YYYY-MM-DD');

ALTER TABLE employees DROP COLUMN hire_date;

--Detect and address any outliers that may skew the analysis.
SELECT 
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    ROUND(AVG(salary), 2) AS avg_salary,
    COUNT(*) AS total_records
FROM employees;

SELECT *
FROM employees
WHERE salary < (SELECT AVG(salary) - 2 * STDDEV(salary) FROM employees)
   OR salary > (SELECT AVG(salary) + 2 * STDDEV(salary) FROM employees);

--Standardize and normalize data where applicable to ensure consistency.

UPDATE employees
SET department = 
    CASE department
        WHEN 'HR' THEN 'Human Resources'
        WHEN 'IT' THEN 'Information Technology'
        ELSE department
    END;

ALTER TABLE employees ADD COLUMN year_hired INTEGER;
ALTER TABLE employees ADD COLUMN salary_level VARCHAR(20);

UPDATE employees
SET year_hired = EXTRACT(YEAR FROM hire_date);

UPDATE employees
SET salary_level = 
    CASE 
        WHEN salary < 60000 THEN 'Entry Level'
        WHEN salary BETWEEN 60000 AND 80000 THEN 'Mid Level'
        ELSE 'Senior Level'
    END;


-- Summary statistics
SELECT 
    COUNT(*) AS total_records,
    COUNT(DISTINCT department) AS unique_departments,
    MIN(hire_date) AS earliest_hire,
    MAX(hire_date) AS latest_hire,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM employees;

-- Verify no NULL values remain
SELECT 
    SUM(CASE WHEN employee_id IS NULL THEN 1 ELSE 0 END) AS null_id,
    SUM(CASE WHEN employee_name IS NULL THEN 1 ELSE 0 END) AS null_name,
    SUM(CASE WHEN salary IS NULL THEN 1 ELSE 0 END) AS null_salary,
    SUM(CASE WHEN hire_date IS NULL THEN 1 ELSE 0 END) AS null_hire_date,
    SUM(CASE WHEN department IS NULL THEN 1 ELSE 0 END) AS null_department
FROM employees;



