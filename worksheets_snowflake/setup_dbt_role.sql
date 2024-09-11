USE ROLE securityadmin;

CREATE ROLE IF NOT EXISTS teacher_dbt_role;

GRANT ROLE teacher_dlt_role to ROLE teacher_dbt_role;

GRANT ROLE teacher_dbt_role TO USER Daniel;
GRANT ROLE teacher_dbt_role TO USER Samuel;
GRANT ROLE teacher_dbt_role TO USER Jacob;
GRANT ROLE teacher_dbt_role TO USER Dimitris_2;
