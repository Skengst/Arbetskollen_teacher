Project jobbannonser_schema {
  database_type: "Snowflake"
}

Table Jobbannonser_Faktatabell {
  ID varchar [pk]
  EXTERNAL_ID varchar
  HEADLINE varchar
  PUBLICATION_DATE timestamp_tz [ref: > Tid_Dimension.PUBLICATION_DATE]
  LAST_PUBLICATION_DATE timestamp_tz [ref: > Tid_Dimension.LAST_PUBLICATION_DATE]
  APPLICATION_DEADLINE timestamp_tz [ref: > Tid_Dimension.APPLICATION_DEADLINE]
  NUMBER_OF_VACANCIES number
  EXPERIENCE_REQUIRED boolean
  ACCESS_TO_OWN_CAR boolean
  DRIVING_LICENSE_REQUIRED boolean
  SALARY_DESCRIPTION varchar [ref: > Lön_Dimension.SALARY_DESCRIPTION]
  RELEVANCE float
  REMOVED boolean
  EMPLOYER__NAME varchar [ref: > Arbetsgivare_Dimension.EMPLOYER__NAME]
  EMPLOYER__ORGANIZATION_NUMBER varchar [ref: > Arbetsgivare_Dimension.EMPLOYER__ORGANIZATION_NUMBER]
  EMPLOYMENT_TYPE__CONCEPT_ID varchar [ref: > Arbetstyp_Dimension.EMPLOYMENT_TYPE__CONCEPT_ID]
  OCCUPATION__CONCEPT_ID varchar [ref: > Yrke_Dimension.OCCUPATION__CONCEPT_ID]
  APPLICATION_DETAILS__EMAIL varchar [ref: > Ansökan_Dimension.APPLICATION_DETAILS__EMAIL]
  DURATION__CONCEPT_ID varchar [ref: > Varaktighet_Dimension.DURATION__CONCEPT_ID]
  DESCRIPTION__TEXT varchar [ref: > Jobbbeskrivning_Dimension.DESCRIPTION__TEXT]

  Note: "Faktatabell för jobbannonser"
}

Table Tid_Dimension {
  TID_ID int [pk]
  PUBLICATION_DATE timestamp_tz
  LAST_PUBLICATION_DATE timestamp_tz
  APPLICATION_DEADLINE timestamp_tz

  Note: "Dimension för tid"
}

Table Arbetsgivare_Dimension {
  ARBETSGIVARE_ID int [pk]
  EMPLOYER__NAME varchar
  EMPLOYER__ORGANIZATION_NUMBER varchar
  EMPLOYER__URL varchar
  EMPLOYER__WORKPLACE varchar
  LOGO_URL varchar

  Note: "Dimension för arbetsgivare"
}

Table Arbetstyp_Dimension {
  ARBETSTYP_ID int [pk]
  EMPLOYMENT_TYPE__CONCEPT_ID varchar
  EMPLOYMENT_TYPE__LABEL varchar
  EMPLOYMENT_TYPE__LEGACY_AMS_TAXONOMY_ID varchar

  Note: "Dimension för arbetstyp"
}

Table Yrke_Dimension {
  YRKE_ID int [pk]
  OCCUPATION__CONCEPT_ID varchar
  OCCUPATION__LABEL varchar
  OCCUPATION__LEGACY_AMS_TAXONOMY_ID varchar
  OCCUPATION_GROUP__CONCEPT_ID varchar
  OCCUPATION_GROUP__LABEL varchar
  OCCUPATION_GROUP__LEGACY_AMS_TAXONOMY_ID varchar
  OCCUPATION_FIELD__CONCEPT_ID varchar
  OCCUPATION_FIELD__LABEL varchar
  OCCUPATION_FIELD__LEGACY_AMS_TAXONOMY_ID varchar

  Note: "Dimension för yrke"
}

Table Ansökan_Dimension {
  ANSÖKAN_ID int [pk]
  APPLICATION_DETAILS__EMAIL varchar
  APPLICATION_DETAILS__INFORMATION varchar
  APPLICATION_DETAILS__OTHER varchar
  APPLICATION_DETAILS__REFERENCE varchar
  APPLICATION_DETAILS__URL varchar
  APPLICATION_DETAILS__VIA_AF boolean

  Note: "Dimension för ansökan"
}

Table Lön_Dimension {
  LÖN_ID int [pk]
  SALARY_TYPE__CONCEPT_ID varchar
  SALARY_DESCRIPTION varchar

  Note: "Dimension för lön"
}

Table Varaktighet_Dimension {
  VARAKTIGHET_ID int [pk]
  DURATION__CONCEPT_ID varchar
  DURATION__LABEL varchar
  DURATION__LEGACY_AMS_TAXONOMY_ID varchar

  Note: "Dimension för varaktighet"
}

Table Jobbbeskrivning_Dimension {
  BESKRIVNING_ID int [pk]
  DESCRIPTION__TEXT varchar
  DESCRIPTION__TEXT_FORMATTED varchar
  DESCRIPTION__CONDITIONS varchar

  Note: "Dimension för jobbbeskrivning"
}