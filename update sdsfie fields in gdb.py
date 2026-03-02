import arcpy
import os

# Set the geodatabase path
arcpy.env.workspace = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\CAFB_SDSFIE.gdb"

# List of fields and their corresponding values to populate
fields_to_update = {
    "baseType": "mainOperatingBase",
    "country": "usa",
    "InstallationID": "eepz",
    "installationID": "eepz",
    "installationSuffix": "afBase",
    "installationName": "columbusAfb",
    "owner": "usaf",
    "majorCommand": "usafa",
    "rpsuid": "1608",
    "siteId": "eepz0001"   
}

# Expression template for calculating field if it's null or empty
expression_template = "calculate(!{field}!)"
code_block_template = '''
def calculate(val):
    if val in (None, "", " "):
        return "{}"
    else:
        return val
'''

# Function to process all feature classes, including those in feature datasets
def process_feature_classes(workspace):
    # List all feature datasets in the workspace
    datasets = arcpy.ListDatasets(feature_type='All')  # Get all feature datasets
    feature_classes = []

    # Get all feature classes inside feature datasets
    for dataset in datasets:
        feature_classes.extend(arcpy.ListFeatureClasses(feature_dataset=dataset))

    # Also get feature classes in the root of the workspace (not inside any datasets)
    feature_classes.extend(arcpy.ListFeatureClasses())

    return feature_classes

# Get all feature classes (including those in datasets)
feature_classes = process_feature_classes(arcpy.env.workspace)

# Loop through each feature class
for fc in feature_classes:
    print(f"Processing: {fc}")
    
    # Get the list of fields in the feature class
    fc_fields = [f.name for f in arcpy.ListFields(fc)]
    
    # Loop through the fields to update
    for field_name, value in fields_to_update.items():
        # Only proceed if the field exists in the feature class
        if field_name in fc_fields:
            print(f"  → Field '{field_name}' exists in {fc}. Updating...")
            
            # Build the expression and code block for CalculateField
            expression = expression_template.format(field=field_name)
            code_block = code_block_template.format(value)
            
            try:
                # Apply the CalculateField function
                arcpy.management.CalculateField(
                    in_table=fc,
                    field=field_name,
                    expression=expression,
                    expression_type="PYTHON3",
                    code_block=code_block,
                    field_type="",
                    enforce_domains="ENFORCE_DOMAINS"
                )
                print(f"    Updated field: {field_name} in {fc}")
            except Exception as e:
                print(f"    ⚠ Error updating field {field_name} in {fc}: {e}")
        else:
            print(f"  → Field '{field_name}' does not exist in {fc}. Skipping...")