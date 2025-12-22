CREATE DATABASE IF NOT EXISTS sales_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE sales_db;

CREATE TABLE sal (
    snum INT PRIMARY KEY,
    sname VARCHAR(50) NOT NULL,
    city VARCHAR(50),
    comm DECIMAL(4,2)
);

INSERT INTO sal (snum, sname, city, comm) VALUES
(1001, 'Peel',     'London',    0.12),
(1002, 'Serres',   'San Jose',  0.13),
(1004, 'Motica',   'London',    0.11),
(1007, 'Rifkin',   'Barcelona', 0.15),
(1003, 'Axelrod',  'New York',  0.10);

CREATE TABLE cust (
    cnum INT PRIMARY KEY,
    cname VARCHAR(50) NOT NULL,
    city VARCHAR(50),
    rating INT,
    snum INT,
    FOREIGN KEY (snum) REFERENCES sal(snum)
);

INSERT INTO cust (cnum, cname, city, rating, snum) VALUES
(2001, 'Hoffman',  'London',    100, 1001),
(2002, 'Giovanni', 'Rome',      200, 1003),
(2003, 'Liu',      'San Jose',  200, 1002),
(2004, 'Grass',    'Berlin',    300, 1002),
(2006, 'Clemens',  'London',    100, 1001),
(2008, 'Cisneros', 'San Jose',  300, 1007),
(2007, 'Pereira',  'Rome',      100, 1004);


CREATE TABLE `ord` (
    onum INT PRIMARY KEY,
    amt DECIMAL(10,2),
    odate DATE,
    cnum INT,
    snum INT,
    FOREIGN KEY (cnum) REFERENCES cust(cnum),
    FOREIGN KEY (snum) REFERENCES sal(snum)
);

INSERT INTO `ord` (onum, amt, odate, cnum, snum) VALUES
(3001, 18.69,   '1990-10-03', 2008, 1007),
(3003, 767.19,  '1990-10-03', 2001, 1001),
(3002, 1900.10, '1990-10-03', 2007, 1004),
(3005, 5160.45, '1990-10-03', 2003, 1002),
(3006, 1098.16, '1990-10-03', 2008, 1007),
(3009, 1713.23, '1990-10-04', 2002, 1003),
(3007, 75.75,   '1990-10-04', 2004, 1002),
(3008, 4723.00, '1990-10-05', 2006, 1001),
(3010, 1309.95, '1990-10-06', 2004, 1002),
(3011, 9891.88, '1990-10-06', 2006, 1001);
