-- responsible for managing user accounts and roles 
USE ROLE securityadmin;

-- role which will be assigned to the user responsible for data loading 
CREATE ROLE IF NOT EXISTS teacher_dlt_role;

GRANT ROLE teacher_dlt_role TO USER Daniel;
GRANT ROLE teacher_dlt_role TO USER Samuel;
GRANT ROLE teacher_dlt_role TO USER Jacob;
GRANT ROLE teacher_dlt_role TO USER Dimitris;


GRANT USAGE ON WAREHOUSE job_ads_wh TO ROLE teacher_dlt_role;

-- allowing the role to access these database objects.
GRANT USAGE ON DATABASE job_ads_db TO ROLE teacher_dlt_role;

-- allowing the role to access these database/staging
GRANT USAGE ON SCHEMA job_ads_db.staging TO ROLE teacher_dlt_role;



-- Transformation / create new tables in the job_ads_db.staging schema.
GRANT CREATE TABLE ON SCHEMA job_ads_db.staging TO ROLE teacher_dlt_role;

-- Data Loading (Load) / Allow the dlt_role to insert, update, and delete data in all existing tables in the staging schema
GRANT INSERT,
UPDATE,
DELETE ON ALL TABLES IN SCHEMA job_ads_db.staging TO ROLE teacher_dlt_role;

-- Allow the dlt_role to insert, update, and delete data in any future tables in the staging schema
GRANT INSERT,
UPDATE,
DELETE ON FUTURE TABLES IN SCHEMA job_ads_db.staging TO ROLE teacher_dlt_role;


-- Data Ingestion (Extract)
-- Grant the ability to read (SELECT) data from all tables in the source schema
GRANT SELECT ON ALL TABLES IN SCHEMA job_ads_db.staging TO ROLE teacher_dlt_role;
GRANT SELECT ON FUTURE TABLES IN SCHEMA job_ads_db.staging TO ROLE teacher_dlt_role; -- reading feature tables



show roles;
SHOW GRANTS TO ROLE teacher_dlt_role;

SHOW GRANTS TO USER teacher_dlt_role;


