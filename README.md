# Ontario Electricity Demand ETL

This Python project uses pandas to turn six sample hourly electricity demand readings into a daily peak summary.

## How it works

- **Extract** reads the hourly data from `daily_demand_practice.csv`.
- **Transform** cleans the column names, converts the date column, and finds the highest demand for each day.
- **Load** saves one row per day to `daily_peak_summary.csv`.

## How to run

Keep `demand_etl.py` and `daily_demand_practice.csv` in the same folder. Open a terminal in that folder and run these commands:

```bash
python -m pip install pandas
python demand_etl.py
```

## Expected output

The script creates `daily_peak_summary.csv` with these contents:

```csv
reading_date,peak_demand_mw
2025-01-01,15600
2025-01-02,16100
```

The peak among the sample readings rose by **500 MW** from January 1 to January 2, 2025. This matches the result verified in R, Power BI, and Tableau.