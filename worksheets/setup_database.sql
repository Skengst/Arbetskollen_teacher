USE ROLE SYSADMIN;

-- Create a new databse
CREATE DATABASE job_ads_db;

--Create new warehouse

CREATE WAREHOUSE IF NOT EXISTS job_ads_wh
    WITH
    WAREHOUSE_SIZE = 'XSMALL'  --the size is xsmall 
    AUTO_SUSPEND = 60           --  Specifies the time in seconds to automatically suspend the warehouse when not in use.
    AUTO_RESUME = TRUE          -- to automatically resume when a query is executed.
    INITIALLY_SUSPENDED = TRUE  -- Start the warehouse in a suspended state
    COMMENT = 'Warehouse for development and analysis database.'; -- comment

CREATE SCHEMA IF NOT EXISTS job_ads_db.staging;
 
SELECT CURRENT_DATABASE(), CURRENT_SCHEMA();

SELECT CURRENT_WAREHOUSE();
