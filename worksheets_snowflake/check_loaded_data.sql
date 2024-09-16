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

SELECT employer_id, employer_name, COUNT(*)
FROM dim_employer
GROUP BY employer_id, employer_name
HAVING COUNT(*) > 1
ORDER BY EMPLOYER_NAME;

SELECT * 
FROM dim_employer
WHERE employer_name = 'Academedia support ab';

SELECT * 
FROM dim_employer
WHERE employer_name = 'Alingsås kommun';