import pandas as pd

# Load your Excel file
# 
df = pd.read_excel(r"C:\Shared\Box\Fed_DOD\USACE-Louisville\W912QR-19-D-0052 - CTI-TPMC-LATA\TO W912QR-20-F-0273 Great Lakes ORC\6.0 Del&Plan Docs\WPAFB\TS899\Supplemental RI Report\Tables\forGIS\PAH_Results.xlsx")

# Step 1: Check if each (Location_ID, Depth) group has a Field Duplicate
has_field_dup = (
    df.groupby(["Location_ID", "Sample_Depth_Interval_ft_bgs"])["Sample_Type"]
      .transform(lambda x: "Field Duplicate" in x.values)
)

# Step 2: Get index of row with highest Results for each (Location_ID, Depth)
idx = (
    df.groupby(["Location_ID", "Sample_Depth_Interval_ft_bgs"])["Results"]
      .idxmax()
)

# Step 3: Keep only those max rows
df_max = df.loc[idx].copy()

# Step 4: Add the Field Duplicate flag
df_max["Has_Field_Duplicate"] = has_field_dup.loc[df_max.index]

# (Optional) Save or view results
df_max.to_excel(r"C:\Shared\Box\Fed_DOD\USACE-Louisville\W912QR-19-D-0052 - CTI-TPMC-LATA\TO W912QR-20-F-0273 Great Lakes ORC\6.0 Del&Plan Docs\WPAFB\TS899\Supplemental RI Report\Tables\forGIS\PAH_Results_clean.xlsx", index=False)

print(df_max)
