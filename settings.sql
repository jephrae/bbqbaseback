-- settings.sql

CREATE DATABASE BBQBASE;
CREATE USER bbqbaseuser WITH PASSWORD 'bbqbase';
GRANT ALL PRIVILEGES ON DATABASE BBQBASE to bbqbaseuser;