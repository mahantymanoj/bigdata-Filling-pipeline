# bigdata-customer-insights-pipeline
bigdata-customer-insights-pipeline

# 🧠 Customer Insights Big Data Pipeline

A full-scale big data engineering project designed to simulate a real-world analytics use case using AWS, Snowflake, PySpark, Redshift, Airflow, DBT, and more.

---

## 🚀 Project Objective

This project aims to build a scalable data pipeline that ingests and processes customer transactions and event logs, transforms the data into meaningful insights, and stores it in Redshift for analysis and reporting.

---


---

## 🧑‍💻 Getting Started

### Prerequisites

- Python 3.8+
- Docker & Docker Compose
- AWS Account
- Snowflake Account
- Git & GitHub

### Installation

###```bash
git clone https://github.com/<your-username>/bigdata-customer-insights-pipeline.git
cd bigdata-customer-insights-pipeline
pip install -r requirements.txt


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

bigdata-customer-insights-pipeline/
│
├── dags/                   # Airflow DAGs
├── dbt/                    # DBT models and configs
│   ├── models/
│   └── profiles.yml
├── glue_jobs/              # PySpark scripts for Glue
├── lambda_functions/       # Lambda handlers
├── data/                   # Sample input data
│   ├── snowflake_exports/
│   └── s3_json_logs/
├── cicd/                   # GitHub Actions workflows
├── terraform/              # (optional) infra as code
├── notebooks/              # Jupyter notebooks (exploration, dev)
├── requirements.txt        # Python dependencies
├── docker-compose.yml      # Local Airflow/DBT setup
└── README.md               # Project overview


🌐 Contributors
Your Name – LinkedIn

Friend's Name – LinkedIn

📌 License
This project is licensed under the MIT License.


