-- 2. Display the names and job titles (ContactTitle) of contacts who are also owners.
SELECT first_name, last_name, job_title
FROM customers
WHERE job_title = 'Owner';

-- 3. Display the names and prices of those products with prices of $50 or more.
SELECT product_name, list_price
FROM products
WHERE list_price >= 50;

-- 4. Display the names and prices of those products with prices in range
SELECT product_name, list_price
FROM products
WHERE list_price BETWEEN 15 AND 20;

-- 5. Display the shipping fee total.
SELECT SUM(shipping_fee) AS total_shipping_fee
FROM orders
GROUP BY customer_id;

-- 6. Display the 05-04-2006 shipping fee total.
SELECT SUM(shipping_fee) AS total_shipping_fee
FROM orders
WHERE shipped_date = '2006-05-04'
GROUP BY customer_id;

-- 7. Display the names of all suppliers and the name of their products.
SELECT s.company AS supplier_name, p.product_name
FROM suppliers s
JOIN products p ON s.id = p.supplier_ids;

-- 8. Display all the suppliers that have a purchase order quantity more than 40.
SELECT s.company AS supplier_name
FROM suppliers s
JOIN purchase_orders po ON s.id = po.supplier_id
JOIN purchase_order_details pod ON po.id = pod.purchase_order_id
WHERE pod.quantity > 40;

-- CREATE TABLE EmpDemo (
--     EmpNo INT AUTO_INCREMENT PRIMARY KEY,
--     Ename VARCHAR(15) NOT NULL,
--     Salary DECIMAL(10,2),  -- MySQL does not support MONEY type
--     DeptNo INT NOT NULL
-- );

-- CREATE TABLE EmpDemo_Log (
--     EmpNo INT,
--     Ename VARCHAR(15),
--     Salary DECIMAL(10,2),
--     DeptNo INT,
--     ActionType VARCHAR(15),  -- Avoid using reserved word "Action"
--     DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );



DELIMITER //

CREATE TRIGGER trg_EmpDemo_Insert
AFTER INSERT ON EmpDemo
FOR EACH ROW
BEGIN
    INSERT INTO EmpDemo_Log (EmpNo, Ename, Salary, DeptNo, ActionType, DateCreated)
    VALUES (NEW.EmpNo, NEW.Ename, NEW.Salary, NEW.DeptNo, 'INSERT', NOW());
END //

CREATE TRIGGER trg_EmpDemo_Update
AFTER UPDATE ON EmpDemo
FOR EACH ROW
BEGIN
    INSERT INTO EmpDemo_Log (EmpNo, Ename, Salary, DeptNo, ActionType, DateCreated)
    VALUES (NEW.EmpNo, NEW.Ename, NEW.Salary, NEW.DeptNo, 'UPDATE', NOW());
END //

CREATE TRIGGER trg_EmpDemo_Delete
AFTER DELETE ON EmpDemo
FOR EACH ROW
BEGIN
    INSERT INTO EmpDemo_Log (EmpNo, Ename, Salary, DeptNo, ActionType, DateCreated)
    VALUES (OLD.EmpNo, OLD.Ename, OLD.Salary, OLD.DeptNo, 'DELETE', NOW());
END //

DELIMITER ;


-- 10. Stored Procedure to Get Employees by DeptNo

DELIMITER //

CREATE PROCEDURE GetEmployeesByDept(IN DeptNo INT)
BEGIN
    IF DeptNo IS NULL THEN
        SELECT * FROM EmpDemo;
    ELSE
        SELECT * FROM EmpDemo WHERE DeptNo = DeptNo;
    END IF;
END //

DELIMITER ;

-- 11. Stored Procedure to Insert Data and Return New EmpNo
DELIMITER //

CREATE PROCEDURE InsertEmployee(
    IN Ename VARCHAR(15),
    IN Salary DECIMAL(10,2),
    IN DeptNo INT,
    OUT NewEmpNo INT
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
    END;

    START TRANSACTION;
    
    INSERT INTO EmpDemo (Ename, Salary, DeptNo)
    VALUES (Ename, Salary, DeptNo);
    
    SET NewEmpNo = LAST_INSERT_ID();
    
    COMMIT;
END //

DELIMITER ;


-- 12. Creating a View and Testing Insert
CREATE VIEW vw_EmpDemo AS
SELECT EmpNo, Ename, Salary, DeptNo FROM EmpDemo;

INSERT INTO vw_EmpDemo (Ename, Salary, DeptNo)
VALUES ('John Doe', 50000, 1);








