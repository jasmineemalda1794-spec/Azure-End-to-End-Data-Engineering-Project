# Azure End-to-End Data Engineering Project


## 📌 Project Overview
This project demonstrates an end-to-end data engineering pipeline built using Microsoft Azure services following the Medallion Architecture (Bronze, Silver, Gold layers).

The pipeline performs data ingestion, transformation, aggregation, and reporting using Azure-native tools.

---

## 🏗 Architecture

Bronze → Silver → Gold architecture:

1. Bronze Layer – Raw data ingestion from CSV into ADLS Gen2
2. Silver Layer – Data cleaning and transformation using Databricks (PySpark)
3. Gold Layer – Aggregated business-ready data
4. External table creation in Synapse Analytics
5. Automated orchestration using Azure Data Factory Trigger

---

## ⚙ Technologies Used

- Azure Data Factory
- Azure Databricks (PySpark)
- Azure Data Lake Storage Gen2
- Azure Synapse Analytics
- GitHub

---

## 🔄 Pipeline Workflow

1. Ingest raw CSV data into Bronze layer
2. Transform data in Databricks notebook
3. Store curated data in Silver layer
4. Aggregate data into Gold layer
5. Query data using Synapse external table
6. Schedule daily execution using ADF Trigger

---

## 📊 Key Features

✔ Medallion Architecture implementation  
✔ Automated pipeline orchestration  
✔ Production-ready cloud setup  
✔ Data transformation using PySpark  
✔ Synapse SQL external table integration  

---

## 📈 Future Enhancements

- Incremental data load
- Data validation checks
- Monitoring & alerting
- CI/CD using Azure DevOps
