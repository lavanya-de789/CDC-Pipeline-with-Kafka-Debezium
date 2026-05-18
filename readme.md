# CDC Pipeline with Kafka + Debezium

## Overview

This project demonstrates an end-to-end Change Data Capture (CDC) architecture built using PostgreSQL, Debezium, Apache Kafka, Spark Structured Streaming, Airflow, and Docker.

The pipeline captures row-level database changes—including inserts, updates, and deletes—from a transactional PostgreSQL database and streams those events in real time through Kafka for downstream processing and analytics.

Instead of repeatedly performing full table loads, the platform captures only incremental changes from database transaction logs and processes them with low latency.

---

## Architecture

```text
PostgreSQL
      ↓
WAL (Write Ahead Log)
      ↓
Debezium Connector
      ↓
Kafka Topic
      ↓
Spark Structured Streaming
      ↓
Bronze Layer
      ↓
Silver Layer
      ↓
Analytics / Warehouse
```

---

## Tech Stack

- Python
- PostgreSQL
- Apache Kafka
- Debezium
- PySpark
- Apache Airflow
- Docker
- Parquet

Optional Extensions:

- Apache Iceberg
- AWS S3
- Snowflake
- Kubernetes
- dbt

---

## Key Features

- Real-time CDC event processing
- Capture insert, update, and delete operations
- Kafka event streaming architecture
- PostgreSQL WAL-based replication
- Spark Structured Streaming transformations
- Bronze and Silver layer implementation
- Airflow workflow orchestration
- Scalable event-driven design

---

## Example CDC Event

```json
{
 "before":{
   "id":1,
   "name":"John"
 },

 "after":{
   "id":1,
   "name":"John Smith"
 },

 "op":"u"
}
```

Operation types:

- c → create
- u → update
- d → delete
- r → snapshot read

---

## Business Use Cases

- Customer profile updates
- Order tracking systems
- Banking transactions
- Inventory monitoring
- Fraud detection
- Real-time analytics