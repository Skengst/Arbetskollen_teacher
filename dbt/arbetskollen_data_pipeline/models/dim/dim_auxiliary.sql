WITH src_auxiliary AS (SELECT * FROM {{ref('src_auxiliary')}})

SELECT 
    {{ dbt_utils.generate_surrogate_key(['id','experience_required'])}} AS auxiliary_attributes_id,
    experience_required,
    driving_license_required,
    car_required,

FROM src_auxiliary