WITH src_employer AS (SELECT * FROM {{ ref('src_employer') }})

{# TODO: fill nulls #}

SELECT
    {{ dbt_utils.generate_surrogate_key(['id', 'employer_name']) }} AS employer_id,
    {{ capitalize_first_letter("coalesce(employer_name, 'ej specificerat')") }} AS employer_name,
    {{ capitalize_first_letter("coalesce(workplace, 'arbetsplats ej specificerad')") }} AS workplace,
    {{ capitalize_first_letter("coalesce(organization_number, 'ej specificerat')") }} AS organization_number,
    {{ capitalize_first_letter("coalesce(url, 'ej specificerat')") }} AS url,
    {{ capitalize_first_letter("coalesce(street_address, 'ej specificerat')") }} AS street_address,
    {{ capitalize_first_letter("coalesce(municipality, 'ej specificerat')") }} AS municipality,
    {{ capitalize_first_letter("coalesce(region, 'ej specificerat')") }} AS region,
    {{ capitalize_first_letter("coalesce(postcode, 'ej specificerat')") }} AS postcode,
    {{ capitalize_first_letter("coalesce(workplace_city, 'ej specificerat')") }} AS workplace_city,
    {{ capitalize_first_letter("coalesce(country, 'ej specificerat')") }} AS country
FROM src_employer