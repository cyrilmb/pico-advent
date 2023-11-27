-- If table exists, delete it
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS contact;
DROP TABLE IF EXISTS address;

-- New table named employee
CREATE TABLE employee (
	id serial PRIMARY KEY,
	fname VARCHAR (25),
	lname VARCHAR (25),
	age INT,
	hiredate DATE
);

-- Data for employee table
INSERT INTO employee (fname, lname, age, hiredate) VALUES
    ('Alan', 'Palmer', 32, '12/15/2019'),
    ('Susan', 'Shepard', 28, '07/21/2015'),
    ('Justin', 'Ward', 43, '08/24/2017'),
    ('Alan', 'Smith', 30, '06/22/2017'),
    ('James', 'Betternot', 26, '06/22/2017'),
    ('Ralph', 'White', 44, '06/23/2017'),
    ('Leonard', 'Nimoy', 72, '12/14/2007'),
    ('Janice', 'Rand', 61, '07/06/2016'),
    ('Harry', 'Mudd', 65, '07/06/2020'),
    ('Hikaru', 'Sulu', 58, '03/21/2015'),
    ('James', 'Kirk', 59, '01/02/2014'),
    ('Leonard', 'McCoy', 65, '08/21/2015'),
    ('Pavel', 'Chekov', 44, '10/15/2014'),
    ('Christopher', 'Pike', 32, '11/24/2014'),
    ('Darth', 'Vader', 124, '03/22/2015'),
    ('Boba', 'Fett', 49, '03/22/2015'),
    ('Luke', 'Skywalker', 66, '11/11/2019'),
    ('Han', 'Solo', 73, '02/03/2012'),
    ('Kylo', 'Ren', 34, '06/14/2020'),
    ('Galen', 'Erso', 55, '06/14/2020');
    
-- New table named address
CREATE TABLE address (
	id serial PRIMARY KEY,
	address1 VARCHAR (45),
	address2 VARCHAR (45),
	city VARCHAR (45),
	state VARCHAR (45),
	zip VARCHAR (15)
);

-- Data for address table
INSERT INTO address (address1, address2, city, state, zip) VALUES
	('1211 Sudan St', 'n/a', 'Mobile', 'AL', '36609'),
	('4800 Barkshire Dr', 'n/a', 'Pace', 'FL', '32571'),
	('12 Nutmeg Ct', 'n/a', 'Culver City', 'CA', '90211'),
	('2142 Elmwood Pl', 'n/a', 'Johnson City', 'TN', '37112'),
	('777 Heavenly Ln', 'Box 13', 'Pike City', 'MN', '50877');

-- New table named contact
CREATE TABLE contact (
	id serial PRIMARY KEY,
	cellphone VARCHAR (15),
	homephone VARCHAR (15),
	email VARCHAR
);

-- Data for contact table
INSERT INTO contact (cellphone, homephone, email) VALUES
	('5121325343', '5125234234', 'apalmer@yachtmail.com'),
	('5129739834', '5129847873', 'sshepard@yorkdevtraining.com'),
	('6453898502', '6459872345',  'jsward2007@yahoo.com'),
	('8763238756', '8763736548', 'alsmith999@gmail.com'),
	('8880345966', '8888567987', 'james.betternot@hotmail.com'),
	('3322827765', '3328760098', 'ralph.white264@aol.com');

-- 	Inner join employee and address tables by id column, return info where fname is Alan
SELECT employee.fname, employee.lname, employee.age, address.city, address.state
FROM employee
INNER JOIN address ON employee.id = address.id 
WHERE fname = 'Alan';

-- Inner employee table to address and contact tables by id column, return infot where email is james.betternot@hotmail.com
SELECT employee.fname, employee.lname, employee.age, address.city, address.state, contact.email
FROM employee
INNER JOIN address ON employee.id = address.id
INNER JOIN contact ON employee.id = contact.id
WHERE email = 'james.betternot@hotmail.com';

-- Change the cellphone variable in contact table where the id equals the id in the employee table where fname is Susan and lname is Shepard
UPDATE contact
SET cellphone = '4383991212'
WHERE id = (SELECT id FROM employee WHERE fname = 'Susan' AND lname = 'Shepard');

-- Join employee table with address and contact tables by id, return all values where fname is Susan and lname is Shepard
SELECT *
FROM employee
JOIN address ON employee.id = address.id
JOIN contact ON employee.id = contact.id
WHERE employee.fname = 'Susan' AND employee.lname = 'Shepard';