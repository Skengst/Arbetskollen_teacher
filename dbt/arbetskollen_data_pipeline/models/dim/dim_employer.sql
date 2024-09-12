WITH src_employer AS (SELECT * FROM {{ ref('src_employer') }})

{# TODO: fill nulls #}

SELECT
    {{ dbt_utils.generate_surrogate_key(['id', 'employer_name']) }} AS employer_id,
    {{ capitalize_first_letter("coalesce(employer_name, 'ej specificerat')") }} AS employer_name,
    {{ capitalize_first_letter("coalesce(workplace, 'arbetsplats ej specificerad')") }} AS employer_workplace,
    {{ capitalize_first_letter("coalesce(organization_number, 'ej specificerat')") }} AS employer_organization_number,
    {{ capitalize_first_letter("coalesce(url, 'ej specificerat')") }} AS employer_url,
    {{ capitalize_first_letter("coalesce(street_address, 'ej specificerat')") }} AS workplace_address_street_address,
    {{ capitalize_first_letter("coalesce(municipality, 'ej specificerat')") }} AS workplace_address_municipality,
    {{ capitalize_first_letter("coalesce(region, 'ej specificerat')") }} AS workplace_address_region,
    {{ capitalize_first_letter("coalesce(postcode, 'ej specificerat')") }} AS workplace_address_postcode,
    {{ capitalize_first_letter("coalesce(city, 'ej specificerat')") }} AS workplace_address_city,
    {{ capitalize_first_letter("coalesce(country, 'ej specificerat')") }} AS workplace_address_country
FROM src_employer