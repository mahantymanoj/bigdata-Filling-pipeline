# bigdata-customer-insights-pipeline
bigdata-customer-insights-pipeline

# 🧠 Customer Insights Big Data Pipeline

A full-scale big data engineering project designed to simulate a real-world analytics use case using AWS, Snowflake, PySpark, Redshift, Airflow, DBT, and more.

---

## 🚀 Project Objective

This project aims to build a scalable data pipeline that ingests and processes customer transactions and event logs, transforms the data into meaningful insights, and stores it in Redshift for analysis and reporting.

---

## 🧱 Tech Stack

- **Python**, **PySpark**
- **AWS**: S3, Lambda, Glue, Athena, Redshift, Step Functions
- **Snowflake**: Source of transactional data
- **DBT**: Data transformation and testing on Redshift
- **Apache Airflow**: Workflow orchestration
- **GitHub Actions**: CI/CD pipeline
- **Docker**: Local development and testing

---

## 🔄 Workflow Overview

1. Export transactional data from **Snowflake** to **S3**.
2. JSON logs (clickstream/cart events) are uploaded to **S3**.
3. **Lambda** triggers **Glue** to process and merge data.
4. Processed data is loaded into **Redshift**.
5. **DBT** builds data models for analytics.
6. **Airflow** orchestrates the entire pipeline.
7. Code is managed and deployed via **GitHub CI/CD**.

---

## 📂 Repository Structure


