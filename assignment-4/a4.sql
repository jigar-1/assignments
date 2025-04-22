-- 2. Display the names (first_name, last_name) using alias "First Name", "Last Name"
SELECT first_name AS "First Name", last_name AS "Last Name" FROM employee;

-- 3. Get unique department IDs from the employee table
SELECT DISTINCT department_id FROM employee;

-- 4. Find the total number of employees in the table
SELECT COUNT(*) AS total_employees FROM employee;

-- 5. Display the average salary of all employees
SELECT AVG(salary) AS average_salary FROM employee;

-- 6. Display the average salary of all employees from each department
SELECT department_id, AVG(salary) AS average_salary FROM employee GROUP BY department_id;

-- 7. Display the sum of salaries of all employees
SELECT SUM(salary) AS total_salary FROM employee;

-- 8. Display the sum of salaries of all employees from each department
SELECT department_id, SUM(salary) AS total_salary FROM employee GROUP BY department_id;

-- 9. Display all employees sorted by last name in descending order
SELECT * FROM employee ORDER BY last_name DESC;

-- 10. Display all employees whose first name contains the character 'e'
SELECT * FROM employee WHERE first_name LIKE '%e%';

-- 11. Display all employees whose last name contains the character '2' two times
SELECT * FROM employee WHERE last_name LIKE '%2%2%';
