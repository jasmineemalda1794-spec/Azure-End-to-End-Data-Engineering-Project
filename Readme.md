# Azure End-to-End Data Engineering Project

Project Overview:

This project demonstrates an end-to-end Azure Data Engineering pipeline built using modern cloud data architecture principles. The solution follows the Medallion Architecture (Bronze → Silver → Gold) design pattern to ingest, transform, and serve data for analytics.

The pipeline automates data ingestion, transformation using PySpark, and loading into curated layers for reporting and analysis.

Architecture:

The project is implemented using the following Azure services:

  -> Azure Data Factory (ADF) – Data ingestion & orchestration
  -> Azure Data Lake Storage Gen2 (ADLS) – Data storage
  -> Azure Databricks – Data transformation using PySpark
  -> Azure Synapse Analytics – Querying curated data
  -> SQL – Data validation & reporting

🔄 Medallion Architecture

Bronze Layer
  Raw data ingestion from source
  Stored in ADLS Gen2
  Minimal transformation

Silver Layer
  Data cleansing
  Handling null values
  Data type standardization
  Business logic transformations

Gold Layer
  Aggregated and curated datasets
  Ready for analytics and reporting
  Optimized for querying
  
## ⚙ Technologies Used

- Azure Data Factory
- Azure Databricks (PySpark)
- Azure Data Lake Storage Gen2
- Azure Synapse Analytics
- GitHub

---
Project Workflow

1️⃣ Data is ingested into the Bronze layer using Azure Data Factory pipelines.
2️⃣ Azure Databricks processes raw data using PySpark transformations.
3️⃣ Cleaned data is written to the Silver layer.
4️⃣ Aggregated datasets are stored in the Gold layer.
5️⃣ Azure Synapse Analytics is used for querying and reporting.

Sample PySpark Transformation:

df = spark.read.format("csv") \
    .option("header", "true") \
    .load("/mnt/bronze/orders.csv")

df_clean = df.dropna() \
    .withColumnRenamed("orderID", "order_id")

df_clean.write.format("parquet") \
    .mode("overwrite") \
    .save("/mnt/silver/orders_clean")

Sample SQL Query (Gold Layer):
      SELECT customer_id,
           SUM(order_amount) AS total_spent
    FROM gold.orders
    GROUP BY customer_id;


Key Skills Demonstrated

✔ ETL Pipeline Design
✔ Cloud Data Engineering
✔ PySpark Transformations
✔ Azure Data Factory Orchestration
✔ Data Lake Architecture
✔ SQL Query Optimization
✔ Medallion Architecture Implementation

---

## 📈 Future Enhancements

- Incremental data load
- Data validation checks
- Monitoring & alerting
- CI/CD using Azure DevOps
