from pathlib import Path
import pandas as pd
# Extract
project_folder = Path(__file__).parent
source_path = project_folder/"daily_demand_practice.csv"
readings =pd.read_csv(source_path,skipinitialspace=True)
# Transform
readings.columns= readings.columns.str.strip()
readings["reading_date"]= pd.to_datetime(readings["reading_date"],format="%Y-%m-%d")
daily_peaks = (readings.groupby("reading_date",as_index= False).agg(peak_demand_mw= ("demand_mw", "max"))
)
# Load (Save)

output_path = project_folder / "daily_peak_summary.csv"
daily_peaks.to_csv(output_path, index=False)
print(f"Saved {len(daily_peaks)} rows to {output_path}")