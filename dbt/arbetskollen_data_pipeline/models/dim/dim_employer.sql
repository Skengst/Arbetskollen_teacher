WITH src_employer AS (SELECT * FROM {{ ref('src_employer') }})

{# TODO: fill nulls #}

SELECT
    *
FROM src_employer;