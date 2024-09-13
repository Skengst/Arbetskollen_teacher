USE ROLE useradmin;
CREATE ROLE IF NOT EXISTS job_ads_reporter_role;

USE ROLE securityadmin;

GRANT USAGE ON WAREHOUSE job_ads_wh TO ROLE job_ads_reporter_role;

GRANT USAGE ON DATABASE job_ads_db TO ROLE job_ads_reporter_role;
GRANT USAGE ON SCHEMA job_ads_db.marts TO ROLE job_ads_reporter_role;
GRANT SELECT ON ALL TABLES IN SCHEMA job_ads_db.marts TO ROLE job_ads_reporter_role;
GRANT SELECT ON ALL VIEWS IN SCHEMA job_ads_db.marts TO ROLE job_ads_reporter_role;
GRANT SELECT ON FUTURE TABLES IN SCHEMA job_ads_db.marts TO ROLE job_ads_reporter_role;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA job_ads_db.marts TO ROLE job_ads_reporter_role;


GRANT ROLE job_ads_reporter_role TO USER daniel;
GRANT ROLE job_ads_reporter_role TO USER samuel;
GRANT ROLE job_ads_reporter_role TO USER dimitris;
GRANT ROLE job_ads_reporter_role TO USER jacob;

USE ROLE job_ads_reporter_role;

SHOW GRANTS TO ROLE job_ads_reporter_role;

-- test querying a mart
USE WAREHOUSE job_ads_wh;
USE DATABASE job_ads_db;
USE SCHEMA job_ads_db.marts;
SHOW VIEWS IN job_ads_db.marts;

SELECT * FROM mart_job_listings LIMIT 10;