import pandas as pd
import os

# ---- INPUTS ----
input_xlsx = r"C:\Users\JoshMcAteer\OneDrive - ctico\Documents\Projects\Duke_Energy\Gibson\Analytes\Arsenic_Nov2025.xlsx"
output_xlsx = r"C:\Users\JoshMcAteer\OneDrive - ctico\Documents\Projects\Duke_Energy\Gibson\Analytes\Arsenic_Nov2025_max.xlsx"
sheet_name = 0  # or sheet name as string

# ---- READ DATA ----
df = pd.read_excel(input_xlsx, sheet_name=sheet_name)

# ---- CREATE SERIES FIELD ----
# Example: MW-12B -> MW-12
df["Series"] = df["WellName"].str[:-1]

# ---- FIND MAX CONCENTRATION PER SERIES ----
max_conc = (
    df.groupby("Series")["Concentration"]
    .max()
    .reset_index()
    .rename(columns={"Concentration": "MaxConcentration"})
)

# ---- JOIN BACK TO ORIGINAL TABLE ----
df = df.merge(max_conc, on="Series", how="left")

# ---- FLAG MAX RECORDS ----
df["IsMax"] = df.apply(
    lambda row: "Yes" if row["Concentration"] == row["MaxConcentration"] else "No",
    axis=1
)

# ---- CLEAN UP ----
df = df.drop(columns=["Series", "MaxConcentration"])

# ---- WRITE OUTPUT ----
df.to_excel(output_xlsx, index=False)

print("Done! Output written to:", output_xlsx)
