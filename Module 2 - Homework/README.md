# � Kestra Workflow Orchestration - NYC Taxi Data Pipeline

**Build and orchestrate data workflows using Kestra with PostgreSQL**

> Part of the Data Engineering Zoomcamp - Module 2 Homework

![Kestra](https://img.shields.io/badge/Kestra-5E4EB6?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHJlY3Qgd2lkdGg9IjEwMCIgaGVpZ2h0PSIxMDAiIGZpbGw9IiM1RTRFQjYiLz48L3N2Zz4=&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

---

## Table of Contents

- [Quick Start](#-quick-start)
- [Project Overview](#-project-overview)
- [Architecture](#-architecture)
  - [Services](#services)
  - [Technology Stack](#-technology-stack)
- [Key Features](#-key-features)

---

## 🚀 Quick Start

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

## 🎯 Architecture

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

## ✨ Key Features

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

## 🎓 Learning Outcomes

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

---

## 📂 Project Files

- **`docker-compose.yaml`** - Service configuration (Kestra, PostgreSQL databases, pgAdmin)
- **`pyproject.toml`** - Python dependencies
- **`ingest_data.py`** - Python script for data ingestion (used by Kestra tasks)
- **`queries.sql`** - SQL queries for analysis
- **`taxi_zone_lookup.csv`** - Reference data

---

## 🔌 Workflow Execution

### Trigger Workflows

1. **In Kestra UI** (`http://localhost:8080`):
   - Navigate to Flows section
   - Create new flow or import existing
   - Click "Execute" to run

2. **Via API**:

```bash
curl -X POST http://localhost:8080/api/v1/executions \
  -H "Content-Type: application/json" \
  -d '{"flowId":"my_flow", "namespace":"default"}'
```

3. **Scheduled**:
   - Define triggers in workflow YAML
   - Kestra scheduler automatically executes

### Monitor Execution

- View real-time progress in UI
- Track task execution times
- Access logs for each step
- Download execution results

---

## 🚀 Next Steps

- Create custom workflows for taxi data processing
- Integrate with external APIs
- Add data validation and quality checks
- Set up monitoring and alerting
- Deploy to production environment

---

## 📚 Resources

- [Kestra Documentation](https://kestra.io/docs/)
- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Compose Guide](https://docs.docker.com/compose/)

---

<div align="center">

**Built with ❤️ for workflow orchestration learning**

[⬆ Back to Top](#-kestra-workflow-orchestration---nyc-taxi-data-pipeline)

</div>

---

## Solution

### Homework Answers

This section contains the solutions to the Data Engineering Zoomcamp Module 1 homework questions.

### Question 1 - Pip Version

**Task:** What's the version of pip in the python:3.13 image?

```bash
docker run -it --entrypoint=bash python:3.13
pip -V
```

**Answer:** `25.3`

---

### Question 2 - pgAdmin Connection

**Task:** Given the docker-compose.yaml, what hostname and port should pgAdmin use to connect to the postgres database?

**Answer:**

- **Container name:** `postgres:5432`
- **Service name:** `db:5432`

Both are correct as Docker creates internal DNS entries for both container names and service names.

---

### Question 3 - Trips ≤ 1 Mile in November 2025

**Task:** For trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01'), how many trips had a trip_distance of ≤ 1 mile?

```sql
SELECT COUNT(*) AS count_trips
FROM public.yellow_taxi_trips
WHERE lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01'
  AND trip_distance <= 1;
```

**Answer:** `8,007 trips`

---

### Question 4 - Pickup Day with Longest Trip Distance

**Task:** Which was the pick up day with the longest trip distance? (Exclude trips > 100 miles)

```sql
SELECT DATE(lpep_pickup_datetime) AS pickup_day
FROM public.yellow_taxi_trips
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;
```

**Answer:** `2025-11-14`

---

### Question 5 - Pickup Zone with Most Trips on November 18

**Task:** Which pickup zone had the most trips on November 18th, 2025?

```sql
SELECT
    tz."Zone" AS pickup_zone,
    COUNT(*) AS trip_count
FROM public.yellow_taxi_trips tt
JOIN public.taxi_zones tz
    ON tz."LocationID" = tt."PULocationID"
WHERE DATE(tt.lpep_pickup_datetime) = '2025-11-18'
GROUP BY tz."Zone"
ORDER BY trip_count DESC
LIMIT 1;
```

**Answer:** `East Harlem North`

---

### Question 6 - Largest Tip from East Harlem North

**Task:** For passengers picked up in "East Harlem North" in November 2025, which dropoff zone had the largest single tip?

```sql
SELECT
    tzd."Zone" AS dropoff_zone,
    MAX(tt.tip_amount) AS largest_tip
FROM public.yellow_taxi_trips tt
JOIN public.taxi_zones tzp
    ON tzp."LocationID" = tt."PULocationID"
JOIN public.taxi_zones tzd
    ON tzd."LocationID" = tt."DOLocationID"
WHERE EXTRACT(MONTH FROM tt.lpep_pickup_datetime) = 11
  AND EXTRACT(YEAR FROM tt.lpep_pickup_datetime) = 2025
  AND tzp."Zone" = 'East Harlem North'
ORDER BY largest_tip DESC
LIMIT 1;
```

**Answer:** `Yorkville West`

---

### Question 7 - Terraform Workflow

**Task:** Describe the Terraform workflow for: (1) downloading provider plugins & setup, (2) generating changes & auto-execute, (3) removing resources

**Answer:**

```
terraform init → terraform apply -auto-approve → terraform destroy
```

---

## 🏗️ Project Description

### Project Overview

This data engineering project implements a production-ready pipeline with the following capabilities:

- ✅ **Automated Data Ingestion**: Downloads and ingests NYC taxi data from GitHub
- ✅ **Database Management**: Uses PostgreSQL for reliable data storage
- ✅ **Container Orchestration**: Docker Compose manages multiple services
- ✅ **Health Checks**: Ensures PostgreSQL is ready before processing
- ✅ **Interactive Analysis**: JupyterLab for data exploration
- ✅ **Web Interface**: pgAdmin for database administration
- ✅ **Scalable Design**: Chunked data loading for memory efficiency

### 🔧 Technology Stack

| Layer                  | Technology     | Purpose                    |
| ---------------------- | -------------- | -------------------------- |
| **Orchestration**      | Docker Compose | Service coordination       |
| **Database**           | PostgreSQL 17  | Data warehouse             |
| **Database UI**        | pgAdmin 4      | Administration interface   |
| **Data Processing**    | Python 3.13    | ETL logic                  |
| **Package Management** | UV             | Fast dependency resolution |
| **Data Analysis**      | JupyterLab     | Interactive notebooks      |
| **ORM**                | SQLAlchemy     | Database abstraction       |
| **Data Manipulation**  | Pandas         | CSV processing             |

### 🎯 Main Components

#### Service Architecture

```
┌─────────────────────────────────────┐
│     Docker Compose Network          │
├─────────────────────────────────────┤
│  pgdatabase (PostgreSQL 17)        │
│  ├── Database: ny_taxi             │
│  └── Tables: yellow_taxi_trips,    │
│            taxi_zones              │
├─────────────────────────────────────┤
│  pgadmin (Database UI)             │
│  ├── Port: 8080                    │
│  └── Access: localhost:8080        │
├─────────────────────────────────────┤
│  data_ingest (Custom Python)       │
│  ├── Downloads taxi data           │
│  └── Populates PostgreSQL          │
├─────────────────────────────────────┤
│  jupyter (JupyterLab)              │
│  ├── Port: 8888                    │
│  └── Data exploration              │
└─────────────────────────────────────┘
```
