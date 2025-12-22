DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS university;

CREATE TABLE university (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    short_name VARCHAR(50) NOT NULL,
    foundation_date DATE NOT NULL
);

CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    university_id INT NOT NULL REFERENCES university(id) ON DELETE CASCADE,
    admission_year INT NOT NULL
);