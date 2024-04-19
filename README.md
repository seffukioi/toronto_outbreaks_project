# TORONTO OUTBREAKS PROJECT

## OBJECTIVE

The objective of this project is to conduct a thorough analysis of historical disease outbreak data in Toronto from 2014 to 2016. By examining key variables such as outbreak settings, types of outbreaks, causative agents, and outbreak durations, the project aims to identify patterns, trends, and risk factors associated with disease outbreaks during this period. The insights gained from this analysis will enable public health authorities to make informed decisions and implement proactive measures to mitigate the impact of future outbreaks.

## TECHNOLOGIES USED

1. Orchestration - Mage
2. Data Lake - Google Cloud Storage
3. Data Warehouse - BigQuery
4. Visualization - Preset(Apache Superset)
5. Transformation - DBT
6. IAC - Terraform

## DATASET

The data used for the project can be fetched from the following dataset
[dataset](https://open.toronto.ca/dataset/outbreaks-in-toronto-healthcare-institutions/)

## PROCEDURE
1. Install and setup terraform
2. Create relevant gcs buckets and bigquery dataset
3. Install and setup mage.
4. Create a mage project
5. Create a data loader to read data from an API
6. Create a data exporter to save the data to google cloud storage
7. Use a query in bigquery to create tables and query data from gcs
8. Install and setup dbt
9. Create dbt transformation for data in bigquery
10. Register and setup preset
11. Create a visualization dashboard 

## VISUALIZATION
The visualization is done using PRESET which uses apache-superset. Attached is an image of the dashboard.
![toronto-disease-outbreaks-2024-04-19T06-41-38 633Z](https://github.com/seffukioi/toronto_outbreaks_project/assets/147942239/0ff8e2b6-29da-4992-a580-5dae52b1efc7)
