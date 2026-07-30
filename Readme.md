# 🏏 Cricket Big Data Project

## Overview

This project demonstrates an end-to-end Data Engineering pipeline using a Live Cricket API, PySpark, Databricks, Delta Lake, and Unity Catalog.

The pipeline follows the Medallion Architecture:

```text
Cricket API
     │
     ▼
 Bronze Layer
 (Raw Data)
     │
     ▼
 Silver Layer
(Cleaned Data)
     │
     ▼
 Gold Layer
(Analytics)
```

---

## Tech Stack

- Python
- PySpark
- Databricks
- Delta Lake
- Unity Catalog
- Spark SQL
- GitHub
- CricAPI

---

## Architecture

### Bronze Layer

Purpose:
- Ingest live cricket data from API
- Store raw JSON response
- Create Bronze Delta Table

Key Operations:
- API Integration
- Raw JSON Storage
- Ingestion Timestamp Tracking

Output:

```text
workspace.default.cricket_bronze_current_matches
```

---

### Silver Layer

Purpose:
- Clean and transform raw data
- Extract useful business fields
- Flatten nested JSON

Transformations:
- Match Details Extraction
- Team Information Extraction
- Score Formatting
- Date Standardization
- Load Timestamp Creation

Output:

```text
workspace.default.cricket_silver_current_matches
```

---

### Gold Layer

Purpose:
- Create business-ready analytics

Analytics Created:

#### Match Type Distribution

```text
T20 Matches
ODI Matches
Test Matches
```

#### Venue-Wise Match Count

```text
Matches Per Venue
```

#### Team-Wise Match Count

```text
Total Matches Played By Each Team
```

#### Summary KPIs

```text
Total Matches
Total Match Types
Total Venues
```

---

## Unity Catalog Usage

Created:

```python
CREATE CATALOG workspace
CREATE SCHEMA workspace.default
CREATE VOLUME workspace.default.cricket_api_project
```

Used for:
- Data Governance
- Organization
- Storage Management

---

## Delta Lake Usage

Used Delta Tables for:

- Bronze Layer
- Silver Layer

Benefits:
- ACID Transactions
- Better Performance
- Schema Enforcement
- Reliable Storage

---

## Project Workflow

```text
Live Cricket API
        │
        ▼
Raw JSON File (Volume)
        │
        ▼
Bronze Delta Table
        │
        ▼
Silver Delta Table
        │
        ▼
Gold Analytics
        │
        ▼
Business Insights
```

---

## GitHub Integration

The project was developed in Databricks and integrated with GitHub for version control.

Features:
- Source Control
- Code Backup
- Version Management
- Collaboration Ready

---

## Key Learnings

- API Integration
- ETL Pipeline Development
- PySpark Transformations
- Delta Lake
- Unity Catalog
- Spark SQL
- Data Aggregation
- GitHub Integration
- Medallion Architecture

---

## Author

Mohammad Furquan

GitHub:
https://github.com/MohammadFurquan