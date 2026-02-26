# Homework 4 - dbt + BigQuery + Looker: Analytics engineering

# Analyses 🗂️

- A place for sql files that you don't want to expose
- Generally used for DQ reports
- Lots of people don't use it

# dbt_project.yml 🗂️

- Most important file in all dbt
- Sets default paths to everything
- Sets prtoject name
- You need it to run dbt commands

# Macros 🗂️

- They behave like python functions (reusable logic). For example conversions. E.g. calculate variable tax rates.
- They help you encapsulate logic in one place
- Tey can be tested

# README.md 🗂️

- Documentation of your project
- Installation/Setup guides
- Links to resources etc.

# Seeds 🗂️

- A space to upload CSVs and flat files to add them to dbt later
- Quick and dirty approach

# Snapshots 🗂️

- Historical snapshot of the data

# Tests 🗂️

- put a sql files as assertions
- If a sql query returns 0 rows then the dbt build will fail
- A place for singular tests

# Models 🗂️

- This is where we put SQL logic
- dbt suggests 3 subfolders:

### staging

- Raw table from database
- Staging files (1 to 1 copy of your data). Minimum cleaning.
  - Data types
  - Renaming columns

### intermediate

- Clean and standardised data
- Anything that is not raw but also not ready to expose

### marts

- Data tat you expose to the end users
- Data ready for consumption
- Tables for dashboards / Properly modelled tables (e.g. star schemas)
