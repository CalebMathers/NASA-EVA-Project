DROP DATABASE IF EXISTS nasa_eva;
CREATE DATABASE nasa_eva;

\c nasa_eva;

CREATE TABLE vehicle (
    vehicle_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    vehicle_name VARCHAR(50)
)