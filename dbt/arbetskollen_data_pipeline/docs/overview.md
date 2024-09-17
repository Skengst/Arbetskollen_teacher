{% docs __overview__ %}

# Job Ad Project

Detta projekt är en del av Arbetskollen-initiativet och syftar till att bygga en datapipeline för att visualisera statistik över jobbannonser. Syftet är att hjälpa studenter och arbetssökande att navigera på arbetsmarknaden och fatta välgrundade beslut om utbildning och karriärval.

> [!NOTE]
> Projektet använder den moderna datastacken och omfattar hela processen från att sätta upp en pipeline, transformera data och visualisera det på en dashboard.

## Projektmål

Målet med projektet är att implementera en modern datapipeline med olika teknologier för att lösa ett verkligt problem. Detta inkluderar att sätta upp Snowflake som ett datalager, tillämpa dimensionell modellering och skapa en dashboard för att visualisera data från jobbannonser.

## Nyckelfunktioner

- **Data Extraction**: Extrahera data från Jobtechs API och ladda in det i Snowflake.
- **Dimensional Modeling**: Förbättra en initial dimensionell modell skapad av en tidigare dataingenjör. Modellen inkluderar tabeller som `dim_employer`, `dim_job_details` och `dim_auxiliary`.
- **Data Transformation**: Använd dbt för att tillämpa transformationer enligt dimensionsmodellen.
- **Testing**: Implementera grundliga datatester i dbt för att säkerställa datakvalitet.
- **Visualization**: Skapa en användarvänlig dashboard som ger insikter om jobbstatistik för olika yrken.

## Dimensionell Modell

![dimensionell modell](assets/dimensional_model.png)
Denna diagram representerar stjärnschemat för jobbannonsens datamodell. Det inkluderar dimensioner som `employer`, `job_details` och `auxiliary` med en faktatabell för `job_ads`.

## What is dbt?
[What is dbt? Documentation](https://github.com/DanielSjoholm/What_is_dbt_documentation/blob/main/README.md)

## Agile Metodologi

Vi följer en Kanban-metod med kontinuerlig förbättring av backloggen. Teamet arbetar med en uppgift i taget för att säkerställa smidigt samarbete och inkrementell framsteg.

## Använda teknologier

- **DLT**: För att ladda all rådata i vårt datalager.
- **Snowflake**: För lagring och hantering av data.
- **DBT**: För transformationer och datatester.
- **Git & GitHub**: För versionskontroll och samarbete i teamet.
- **Streamlit**: För att bygga den slutgiltiga dashboarden som visar jobbstatistik.

{% enddocs %}