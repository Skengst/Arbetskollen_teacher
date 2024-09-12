USE ROLE USERADMIN; -- is responsible for managing user/accounts/roles

CREATE USER IF NOT EXISTS Daniel --  this user will be responsible for the extraction and loading processes,
PASSWORD = 'Password1#'
LOGIN_NAME = 'Daniel'
MUST_CHANGE_PASSWORD = true
DEFAULT_WAREHOUSE = job_ads_wh;

CREATE USER Samuel
PASSWORD = 'Password2#' -- changed to Passworddbtrole123##
LOGIN_NAME = 'Samuel'
MUST_CHANGE_PASSWORD = true
DEFAULT_WAREHOUSE = job_ads_wh;

CREATE USER Jacob
PASSWORD = 'Password3#'
LOGIN_NAME = 'Jacob'
MUST_CHANGE_PASSWORD = true
DEFAULT_WAREHOUSE = job_ads_wh;

SHOW USERS;

drop user dbt_user;

CREATE USER Dimitris_2
PASSWORD = 'Password4#'
LOGIN_NAME = 'Dimitris_2'MUST_CHANGE_PASSWORD = true
DEFAULT_WAREHOUSE = job_ads_wh;
