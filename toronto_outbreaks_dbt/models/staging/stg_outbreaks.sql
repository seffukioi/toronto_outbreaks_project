{{ config(materialized='table') }}

with 

source as (

    select * from {{ source('staging', 'outbreaks') }}

),

renamed as (

    select
        Institution_Name,
        Institution_Address,
        Outbreak_Setting,
        Type_of_Outbreak,
        coalesce(Causative_Agent_1,Causative_Agent___1) Causative_Agent_1,
        coalesce(Causative_Agent_2,Causative_Agent___1) Causative_Agent_2,
        Date_Outbreak_Began,
        Date_Declared_Over,
        DATE_DIFF(coalesce(Date_Declared_Over,CURRENT_DATE()), Date_Outbreak_Began, DAY) AS outbreak_duration
        -- DATE_DIFF(coalesce(TO_DATE(Date_Declared_Over, 'YYYY-MM-DD'),CURRENT_DATE()), TO_DATE(Date_Outbreak_Began, 'YYYY-MM-DD')) AS outbreak_duration
        -- DATE_DIFF(coalesce(CAST(Date_Declared_Over AS DATE),CURRENT_DATE()), CAST(Date_Outbreak_Began AS DATE)) AS outbreak_duration

    from source

)

select * from renamed