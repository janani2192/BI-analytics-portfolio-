# Sales Opportunity Anomaly Detection Pipeline

## Overview
This project demonstrates a real-world Business Intelligence and Advanced Analytics workflow designed for Sales Operations and Finance teams.

The pipeline:
- Generates and ingests opportunity-level data
- Performs data cleaning and feature engineering
- Applies machine learning (Isolation Forest) for anomaly detection
- Flags unusual or risky deals
- Adds automated business explanations
- Outputs BI-ready tables for dashboarding

## Business Problem
Sales leaders often manage thousands of open deals and struggle to proactively identify:

- Over-discounted opportunities
- Stalled deals sitting too long in a stage
- Large deals with low win probability
- Data quality gaps (e.g., Unknown regions)

This solution surfaces high-risk opportunities for pipeline reviews and forecasting.

## Tech Stack
- Python
- Pandas
- Scikit-learn
- GitHub
- CLI automation
- Tableau (downstream visualization)

## Pipeline Flow
Raw Opportunity Data ➝ Cleaning ➝ Feature Engineering ➝ ML Modeling ➝ Anomaly Scoring ➝ Explainability ➝ BI Output

## Output Artifact
`data/opportunity_anomaly_scores.csv`

Contains:
- anomaly_score
- is_anomaly
- anomaly_reason

## Example Business Use Cases
- Weekly pipeline risk reviews
- Deal desk prioritization
- Forecast adjustments
- Audit & compliance checks
- Sales ops monitoring dashboards

## Future Enhancements
- API ingestion from CRM systems
- Scheduled orchestration
- Warehouse loading (BigQuery / Snowflake)
- Tableau dashboards
- Alerting via email or Slack


