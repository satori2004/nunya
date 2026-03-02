import pandas as pd

# ---- INPUTS ----
input_table = r"C:\Users\JoshMcAteer\OneDrive - ctico\Documents\Projects\Duke_Energy\Gibson\Analytes\Cobolt_Nov2025.xlsx"
output_table = r"C:\Users\JoshMcAteer\OneDrive - ctico\Documents\Projects\Duke_Energy\Gibson\Analytes\Cobolt_Nov2025_labels.xlsx"

# ---- READ INPUT ----
df = pd.read_excel(input_table)

# ---- PARSE SERIES + POSITION ----
df["Series"] = df["WellName"].str[:-1]          # MW-12A -> MW-12
df["Position"] = df["WellName"].str[-1].str.upper()  # A / B / C

# ---- FIND MAX CONCENTRATION PER SERIES ----
df["MaxConc"] = df.groupby("Series")["Concentration"].transform("max")

# ---- FLAG MAX RECORD ----
df["IsMax"] = df["Concentration"] == df["MaxConc"]

# ---- FORMAT CONCENTRATION TEXT ----
def format_value(row):
    if not row["Detected"]:
        return f"<{row['DetectionLimit']}"
    return str(row["Concentration"])

df["CO_Text"] = df.apply(format_value, axis=1)

# ---- BUILD OUTPUT RECORDS ----
output_rows = []

for series, g in df.groupby("Series"):
    row = {
        "Loc_ID": g["Lable For Map"].iloc[0],
        "A_CO": "",
        "B_CO": "",
        "C_CO": "",
        "CO_A_Label": "",
        "CO_B_Label": "",
        "CO_C_Label": ""
    }

    for _, r in g.iterrows():
        pos = r["Position"]
        row[f"{pos}_CO"] = r["CO_Text"]

        if r["IsMax"]:
            row[f"CO_{pos}_Label"] = "MAX"

    output_rows.append(row)

# ---- CREATE OUTPUT TABLE ----
out_df = pd.DataFrame(output_rows)

# ---- WRITE OUTPUT ----
out_df.to_excel(output_table, index=False)

print("Output table created:", output_table)
