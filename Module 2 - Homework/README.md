# Kestra Workflow Orchestration - NYC Taxi Data Pipeline

**Build and orchestrate data workflows using Kestra with PostgreSQL**

> Part of the Data Engineering Zoomcamp - Module 2 Homework

![Kestra](https://img.shields.io/badge/Kestra-5E4EB6?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHJlY3Qgd2lkdGg9IjEwMCIgaGVpZ2h0PSIxMDAiIGZpbGw9IiM1RTRFQjYiLz48L3N2Zz4=&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

---

## Table of Contents

- [Homework Questions & Answers](#homework-questions--answers)
- [Project Overview](#project-overview)
  - [Quick Start](#-quick-start)
  - [Architecture](#-architecture)
  - [Key Features](#-key-features)
  - [Learning Outcomes](#-learning-outcomes)

---

## ❓ Homework Questions & Answers

1. Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?

_Solution:_

One of the ways to check the output file size is to run the following command in the Google Cloud Shell:

```shell
gcloud storage ls gs://bucket-kestra_090122312/yellow_tripdata_2020-12.csv --long
```

_Answer:_ 128.3 MiB

2. What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?

Solution:
This information can be cocated in the executionas tab by location the correct execution and checking Inputs section ong the Overview tab

Answer:
green_tripdata_2020-04.csv

3. How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?

Solution:
To get thisd information you can run the following SQL query directly on 'yellow_tripdata' table on BigQuery table

```sql
SELECT  COUNT(*) FROM `zoomcamp.yellow_tripdata`
WHERE filename LIKE "%2020%"
```

Answer: 24,648,499

4. How many rows are there for the Green Taxi data for all CSV files in the year 2020?

Same as Question 3 but for green taxi data:

```sql
SELECT  COUNT(*) FROM `zoomcamp.green_tripdata`
WHERE filename LIKE "%2020%"
```

Answer: 1,734,051

5. How many rows are there for the Yellow Taxi data for the March 2021 CSV file?

Here is the SQL solution:

```sql
SELECT  COUNT(*) FROM `zoomcamp.yellow_tripdata`
WHERE filename LIKE "%2021-03%"
```

Answer: 1,925,152

6. How would you configure the timezone to New York in a Schedule trigger?

According to Kestra documentation timezone is defined as UTC time zone identifier. We can add a timezone property to the trigers in Kestra Flow yaml definition:

```yaml
- id: yellow_schedule
  type: io.kestra.plugin.core.trigger.Schedule
  cron: "0 10 1 * *"
  timezone: UTC-5
  inputs:
    taxi: yellow
```

Answer:
Add a timezone property set to UTC-5 in the Schedule trigger configuration

## Project Overview

### Prerequisites

- Docker and Docker Compose installed
- 2GB+ free disk space

### Setup & Run

```bash
# Start all services
docker compose up -d

# Access Kestra UI
open http://localhost:8080

# Access pgAdmin
open http://localhost:8083
```

### Service Endpoints

| Service         | URL                     | Credentials                                   |
| --------------- | ----------------------- | --------------------------------------------- |
| **Kestra**      | `http://localhost:8080` | Email: `admin@kestra.io` / Pass: `Admin1234!` |
| **pgAdmin**     | `http://localhost:8083` | Email: `admin@admin.com` / Pass: `root`       |
| **NYC Taxi DB** | `localhost:5422`        | User: `root` / Pass: `root`                   |
| **Kestra DB**   | `localhost:5431`        | User: `kestra` / Pass: `k3str4`               |

### Connect to PostgreSQL via pgAdmin

In pgAdmin, add a new server:

- **Name:** `ny_taxi` (or your choice)
- **Host:** `pgdatabase` (Docker container name)
- **Port:** `5432` (internal container port)
- **Username:** `root`
- **Password:** `root`
- **Database:** `ny_taxi`

---

## 🏗️ Project Overview

This module introduces **Kestra**, a modern workflow orchestration platform for building and executing data pipelines. Instead of manually running Python scripts or SQL queries, Kestra allows you to:

✅ **Declaratively Define Workflows** - YAML-based pipeline definitions
✅ **Schedule & Trigger Execution** - Run workflows on schedules or events
✅ **Monitor & Debug** - Beautiful UI for tracking execution and troubleshooting
✅ **Parallelize Tasks** - Execute steps concurrently for efficiency
✅ **Version Control** - Commit workflows like code
✅ **Integrate Multiple Systems** - Connect to databases, APIs, file systems, etc.

### What This Project Demonstrates

- Setting up Kestra with Docker Compose
- Creating workflows that ingest NYC taxi data into PostgreSQL
- Orchestrating multi-step ETL pipelines
- Monitoring and debugging workflow execution
- Managing dependencies between tasks

---

### 🚀 Quick Start

#### Prerequisites

- Docker and Docker Compose installed
- 2GB+ free disk space

#### Setup & Run

```bash
# Start all services
docker compose up -d

# Access Kestra UI
open http://localhost:8080

# Access pgAdmin
open http://localhost:8083
```

#### Service Endpoints

| Service         | URL                     | Credentials                                   |
| --------------- | ----------------------- | --------------------------------------------- |
| **Kestra**      | `http://localhost:8080` | Email: `admin@kestra.io` / Pass: `Admin1234!` |
| **pgAdmin**     | `http://localhost:8083` | Email: `admin@admin.com` / Pass: `root`       |
| **NYC Taxi DB** | `localhost:5422`        | User: `root` / Pass: `root`                   |
| **Kestra DB**   | `localhost:5431`        | User: `kestra` / Pass: `k3str4`               |

#### Connect to PostgreSQL via pgAdmin

In pgAdmin, add a new server:

- **Name:** `ny_taxi` (or your choice)
- **Host:** `pgdatabase` (Docker container name)
- **Port:** `5432` (internal container port)
- **Username:** `root`
- **Password:** `root`
- **Database:** `ny_taxi`

---

### 🎯 Architecture

### Services

```
┌─────────────────────────────────────────────────┐
│        Docker Compose Network                   │
├─────────────────────────────────────────────────┤
│ Kestra Server (Workflow Engine)                │
│ ├── Port: 8080 (UI)                            │
│ ├── Executes workflows in Docker               │
│ └── Stores execution history in PostgreSQL     │
├─────────────────────────────────────────────────┤
│ Kestra PostgreSQL Database                      │
│ ├── Stores workflows, executions, configs      │
│ ├── Host Port: 5431                            │
│ └── Container Port: 5432                       │
├─────────────────────────────────────────────────┤
│ NYC Taxi PostgreSQL Database                    │
│ ├── Data warehouse for taxi data               │
│ ├── Host Port: 5422                            │
│ └── Container Port: 5432                       │
├─────────────────────────────────────────────────┤
│ pgAdmin                                         │
│ ├── Database management UI                     │
│ ├── Port: 8083                                 │
│ └── Connect to both databases                  │
└─────────────────────────────────────────────────┘
```

### 🔧 Technology Stack

| Layer                      | Technology     | Purpose                                 |
| -------------------------- | -------------- | --------------------------------------- |
| **Workflow Orchestration** | Kestra v1.1    | Define, schedule, and execute pipelines |
| **Workflow Storage**       | PostgreSQL 18  | Store workflows and execution history   |
| **Data Warehouse**         | PostgreSQL 18  | NYC taxi data storage                   |
| **Database UI**            | pgAdmin 4      | Database management and exploration     |
| **Containerization**       | Docker Compose | Multi-service orchestration             |

---

### ✨ Key Features

### Workflow Orchestration

Kestra replaces manual script execution with declarative, monitored workflows:

```yaml
# Example workflow structure (YAML)
id: ingest_nyc_taxi_data
namespace: dataeng

tasks:
  - id: download_data
    type: http.download
    url: https://example.com/taxi_data.csv

  - id: load_to_postgres
    type: io.kestra.plugin.sqlquery
    sql: "INSERT INTO yellow_taxi_trips SELECT * FROM staging"

  - id: verify
    type: io.kestra.plugin.sqlquery
    sql: "SELECT COUNT(*) FROM yellow_taxi_trips"
```

### Benefits Over Module 1

| Aspect                  | Module 1 (Docker)                | Module 2 (Kestra)            |
| ----------------------- | -------------------------------- | ---------------------------- |
| **Workflow Definition** | Python script + manual execution | YAML-based, declarative      |
| **Scheduling**          | Manual or cron jobs              | Built-in scheduling engine   |
| **Monitoring**          | Logs only                        | Web UI with execution graph  |
| **Error Handling**      | Manual try/catch                 | Automatic retry logic        |
| **Parallelization**     | Manual threading                 | Native parallel tasks        |
| **State Management**    | Files/environment                | Persistent state in database |

---

### 🎓 Learning Outcomes

This module demonstrates:

🎯 **Workflow Orchestration Concepts**

- DAG (Directed Acyclic Graph) design patterns
- Task dependencies and execution order
- Conditional execution and branching

🎯 **Kestra Platform**

- Workflow definition and deployment
- Task types and plugin system
- Execution monitoring and debugging
- Flow triggers and scheduling

🎯 **Data Pipeline Best Practices**

- Idempotent pipeline design
- Error handling and retries
- Data validation and quality checks
- Logging and observability
