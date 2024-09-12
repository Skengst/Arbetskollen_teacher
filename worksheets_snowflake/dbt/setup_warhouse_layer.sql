USE ROLE SYSADMIN;

USE DATABASE job_ads_db;

CREATE SCHEMA IF NOT EXISTS job_ads_db.warehouse;

USE ROLE securityadmin;

GRANT USAGE, CREATE TABLE, CREATE VIEW ON SCHEMA job_ads_db.warehouse TO ROLE teacher_dbt_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA job_ads_db.warehouse TO ROLE teacher_dbt_role;
GRANT SELECT ON ALL VIEWS IN SCHEMA job_ads_db.warehouse TO ROLE teacher_dbt_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON FUTURE TABLES IN SCHEMA job_ads_db.warehouse TO ROLE teacher_dbt_role;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA job_ads_db.warehouse TO ROLE teacher_dbt_role;



-- manual test
USE ROLE teacher_dbt_role;
SHOW GRANTS ON SCHEMA job_ads_db.warehouse;
USE SCHEMA job_ads_db.warehouse;
CREATE TABLE test (id INTEGER);
SHOW TABLES;
DROP TABLE TEST;