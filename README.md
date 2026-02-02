# PMIS Data Integration & Analytics Dashboard

## Overview
This project demonstrates a PMIS-style data integration and analytics workflow
similar to those used in large construction and infrastructure programs.

The solution simulates extracting project data from a PMIS system using REST APIs,
transforming it into analytics-ready datasets, and visualising KPIs in Power BI.

## Business Context
Project Management Information Systems (PMIS) such as PM Web, Unifier, and ACC
store large volumes of project data, including transmittals, submittals, RFIs,
and approvals. Efficient extraction and reporting of this data is critical for
project controls and decision-making.

## Architecture
PMIS API (Mock JSON)
        ↓
Python Data Extraction
        ↓
Data Transformation & Validation
        ↓
CSV Output
        ↓
Power BI Dashboard

## Features
- Simulated PMIS REST API data extraction
- Data cleansing and transformation
- KPI-ready CSV outputs
- Power BI dashboard for approval cycle time and overdue tracking

## Technologies Used
- Python
- REST API concepts
- JSON / CSV
- Power BI
- Construction PMIS concepts

## KPIs Visualised
- Total transmittals by status
- Approval cycle time
- Overdue items
- Discipline-wise document distribution

## Disclaimer
This is a simulated project created for technical demonstration purposes only.
No real client or project data has been used.
