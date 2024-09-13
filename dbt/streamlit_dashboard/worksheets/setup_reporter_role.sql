USE ROLE useradmin;
CREATE ROLE IF NOT EXISTS job_ads_reporter_role;

USE ROLE securityadmin;

GRANT USAGE ON WAREHOUSE compute_wh TO ROLE job_ads_reporter_role;

GRANT USAGE ON DATABASE job_ads TO ROLE job_ads_reporter_role;
GRANT USAGE ON SCHEMA job_ads.marts TO ROLE job_ads_reporter_role;
GRANT SELECT ON ALL TABLES IN SCHEMA job_ads.marts TO ROLE job_ads_reporter_role;
GRANT SELECT ON ALL VIEWS IN SCHEMA job_ads.marts TO ROLE job_ads_reporter_role;
GRANT SELECT ON FUTURE TABLES IN SCHEMA job_ads.marts TO ROLE job_ads_reporter_role;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA job_ads.marts TO ROLE job_ads_reporter_role;


GRANT ROLE job_ads_reporter_role TO USER daniel;
GRANT ROLE job_ads_reporter_role TO USER samuel;
GRANT ROLE job_ads_reporter_role TO USER dimitris;
GRANT ROLE job_ads_reporter_role TO USER jacob;

USE ROLE job_ads_reporter_role;

SHOW GRANTS TO ROLE job_ads_reporter_role;

-- test querying a mart
USE WAREHOUSE compute_wh;
USE DATABASE job_ads;
USE SCHEMA job_ads.marts;
SHOW VIEWS IN job_ads.marts;
SELECT * FROM mart_job_listnings LIMIT 10;