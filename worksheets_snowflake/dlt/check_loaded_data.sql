USE ROLE TEACHER_DLT_ROLE;

USE WAREHOUSE job_ads_wh;

USE DATABASE job_ads_db;

USE SCHEMA staging;

SELECT COUNT(*) AS AmountOfRows FROM jobsearch_teacher_data;

USE ROLE TEACHER_DBT_ROLE;

USE WAREHOUSE job_ads_wh;

USE DATABASE job_ads_db;

USE SCHEMA WAREHOUSE;

SELECT employer_id, COUNT(*)
FROM dim_employer
GROUP BY employer_id
HAVING COUNT(*) > 1;