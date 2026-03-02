import re
import pandas as pd

# -----------------------------
# Input list
# -----------------------------
shapefiles = [
'SS028_Area_B_OCT23_TCE_scrub',
'SS028_Area_B_OCT23_TCE',
'SS028_Area_B_OCT23_TCE_scrub2',
'SS028_Oct_23_TCE_C',
'SS028_Area_C_OCT23_TCE_scrub',
'SS028_Area_C_OCT23_VC_scrub',
'SS028_Area_C_OCT23_VC',
'SS028_Area_E_OCT23_VC_scrub',
'SS028_Area_E_OCT23_VC',
'SS028_Area_E_OCT23_TCE_scrub',
'SS028_Area_E_OCT23_TCE',
'CAFB_OCT2023_COC',
'MW06TCE_1023',
'MW06_VC_1023',
'MW06_VC_1023_orig',
'W128_TCE_1023',
'W128_VC_1023',
'SS028_Area_A_OCT23_VC_Jun24Revise',
'SS028_Area_E_OCT23_TCE_Jun24Rev',
'Contour_SS028_A_VC_1024',
'Contour_SS028_B_TCE_1_Buffer',
'VC2021Plume',
'Contour_SSI_TCE1',
'SS028_May2022_TCE_Area_B',
'SS028_May2022_TCE_Area_B_Merged',
'SS028_May2022_VC_Area_B',
'SS028_May2022_VC_Area_B_merged',
'SS028_May2022_VC_AreaA',
'SS028_May2022_VC_AreaA_merged',
'SS028May2022_AreaC',
'SS028_May2022_VC_Area_C',
'SS028_May2022_VC_Area_C_merged',
'SS028_May2022_TCE_Area_C',
'SS028_May2022_TCE_Area_C_merged',
'SS028_May2022_TCE_Area_E',
'SS028_May2022_TCE_Area_E_pol',
'SS028_May2022_VC_Area_E',
'SS028_May2022_VC_Area_E_merge',
'SS028_May2022_TCE_Area_E_merge',
'SS032_MW06_May2022_VC_Oct',
'SS032_MW06_May2022_VC_Merge',
'SS032_W128_May2022_TCE',
'SS032_W128_May2022_TCE_merge',
'SS032_W128_May2022_VC',
'SS028_May2022_Area_E_COCs',
'SS028_TCE_VC_Oct2022',
'SS028_TCE_Area_A_Plume',
'SS028_VC_Area_A_Plume',
'SS028_TCE_Area_C_Plume',
'SS028_TCE_Area_C_Plume_adj',
'SS028_VC_Area_C_Plume',
'SS028_TCE_Area_B_Plume',
'SS028_TCE_Area_B_Plume_adj',
'SS028_TCE_Area_B_Plume_scrubbed',
'SS028_VC_Area_B_Plume',
'SS028_VC_Area_E_Plume',
'SS028_TCE_Area_E_Plume',
'SS032_TCE_VC_Oct2022',
'SS032_TCE_MW06_Plume',
'SS032_VC_W128_Plume',
'SS032_TCE_W128_Plume',
'SS032_VC_MW06_Plume',
'CVOC_Plume102022',
'SS032_May2023_VC',
'Area_B_May2023_VC',
'Area_B_May2023_TCE',
'Area_B_May2023_TCE_5',
'Area_B_May2023_TCE_Scrubbed',
'Area_B_May2023_VC_Scrubbed',
'October_2022_TCE',
'May_2022_TCE',
'COC_Plume'
]

# -----------------------------
# Helper Functions
# -----------------------------

def extract_date(name):
    # Match formats like OCT23, 1023, Oct2022, May2022, 2021
    patterns = [
        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[_]?\d{2,4}',
        r'\b\d{4}\b',
        r'\b\d{2}23\b',  # 1023 style
        r'\b\d{6}\b'
    ]
    for pattern in patterns:
        match = re.search(pattern, name, re.IGNORECASE)
        if match:
            return match.group(0)
    return "Unknown"


def extract_analyte(name):
    analytes = ['TCE', 'VC', 'COC', 'COCs', 'CVOC']
    
    # Split filename into clean tokens
    tokens = re.split(r'[^A-Za-z0-9]+', name.upper())
    
    found = [a for a in analytes if a in tokens]
    
    if not found:
        return "Not specified"
    
    return " & ".join(sorted(set(found)))


def extract_site(name):
    # Capture SS###, MW##, W###, CAFB, SSI, Area_X
    patterns = [
        r'SS\d{3}',
        r'MW\d{2}',
        r'W\d{3}',
        r'CAFB',
        r'SSI'
    ]
    for pattern in patterns:
        match = re.search(pattern, name, re.IGNORECASE)
        if match:
            return match.group(0).upper()
    
    # Area-only cases
    area_match = re.search(r'Area[_ ]?[A-Z]', name, re.IGNORECASE)
    if area_match:
        return area_match.group(0).replace("_", " ")
    
    return "Unknown"


# -----------------------------
# Parse Data
# -----------------------------

records = []

for shp in shapefiles:
    site = extract_site(shp)
    date = extract_date(shp)
    analyte = extract_analyte(shp)
    
    records.append({
        "Shapefile": shp,
        "Site": site,
        "Date": date,
        "Analyte": analyte
    })

df = pd.DataFrame(records)

# -----------------------------
# Output
# -----------------------------

print(df)

# Optional: export to CSV
# df.to_csv("parsed_shapefiles.csv", index=False)