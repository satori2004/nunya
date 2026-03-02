
import pandas as pd

# --------------------------------------------------
# INPUTS
# --------------------------------------------------
input_excel = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\Crosswalk\EnvRestorationSample_working_input.xlsx"
output_excel = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\Crosswalk\EnvRestorationSample_working_consolidated.xlsx"

# --------------------------------------------------
# STEP 1 — READ EXCEL
# --------------------------------------------------
df = pd.read_excel(input_excel)

print("Original record count:", len(df))
print("Unique Feature Name count:", df["Feature Name"].nunique())

# --------------------------------------------------
# STEP 2 — DEFINE FIRST NON-NULL FUNCTION
# --------------------------------------------------
def first_valid(series):
    for val in series:
        if pd.notnull(val) and str(val).strip() != "":
            return val
    return None

# --------------------------------------------------
# STEP 3 — GROUP AND CONSOLIDATE
# --------------------------------------------------
grouped_df = df.groupby("Feature Name", as_index=False).agg(first_valid)

print("Final consolidated record count:", len(grouped_df))

# --------------------------------------------------
# STEP 4 — WRITE NEW EXCEL
# --------------------------------------------------
grouped_df.to_excel(output_excel, index=False)

print("Consolidation complete.")

