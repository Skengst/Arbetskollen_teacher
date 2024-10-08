USE ROLE SYSADMIN;

USE DATABASE JOB_ADS_DB;  

CREATE SCHEMA IF NOT EXISTS marts;

SHOW SCHEMAS IN DATABASE job_ads_db;

USE ROLE SECURITYADMIN;

GRANT USAGE,
CREATE TABLE,
CREATE VIEW ON SCHEMA JOB_ADS_DB.marts TO ROLE teacher_dbt_role;

-- grant CRUD and select tables and views
GRANT SELECT,
INSERT,
UPDATE,
DELETE ON ALL TABLES IN SCHEMA JOB_ADS_DB.marts TO ROLE teacher_dbt_role;
GRANT SELECT ON ALL VIEWS IN SCHEMA JOB_ADS_DB.marts TO ROLE teacher_dbt_role;

-- grant CRUD and select on future tables and views
GRANT SELECT,
INSERT,
UPDATE,
DELETE ON FUTURE TABLES IN SCHEMA JOB_ADS_DB.marts TO ROLE teacher_dbt_role;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA JOB_ADS_DB.marts TO ROLE teacher_dbt_role;

-- manual test
USE ROLE teacher_dbt_role;
USE SCHEMA JOB_ADS_DB.marts;
CREATE TABLE test (id INTEGER);
SHOW TABLES;
DROP TABLE TEST;

-------------


select current_user();