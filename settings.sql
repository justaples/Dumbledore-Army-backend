-- settings.sql
CREATE DATABASE daspelltracker;
CREATE USER dauser WITH PASSWORD 'da-spell-tracker';
GRANT ALL PRIVILEGES ON DATABASE daspelltracker TO dauser;
