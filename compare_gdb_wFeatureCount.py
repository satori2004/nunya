import arcpy

def compare_feature_classes_and_counts(gdb1, gdb2):
    """
    Compare the feature classes (by name) and their record counts in two geodatabases.
    
    Parameters:
    - gdb1: Path to the first geodatabase
    - gdb2: Path to the second geodatabase
    
    Returns:
    - A message indicating whether the feature classes are identical and if their counts match.
    """
    
    # Get the feature classes from both geodatabases
    feature_classes_gdb1 = arcpy.ListFeatureClasses("*", "ALL", gdb1) or []  # Return empty list if None
    feature_classes_gdb2 = arcpy.ListFeatureClasses("*", "ALL", gdb2) or []  # Return empty list if None
    
    # Step 1: Compare the feature classes between the two geodatabases
    feature_classes_gdb1_set = set(feature_classes_gdb1)
    feature_classes_gdb2_set = set(feature_classes_gdb2)
    
    # Compare the two sets to find differences
    missing_in_gdb2 = feature_classes_gdb1_set - feature_classes_gdb2_set
    missing_in_gdb1 = feature_classes_gdb2_set - feature_classes_gdb1_set
    
    # Print the feature classes that are missing in each geodatabase
    if missing_in_gdb2:
        print(f"Feature classes present in GDB1 but not GDB2: {missing_in_gdb2}")
    if missing_in_gdb1:
        print(f"Feature classes present in GDB2 but not GDB1: {missing_in_gdb1}")
    
    # Step 2: Compare the feature counts for matching feature classes
    for feature_class in feature_classes_gdb1_set.intersection(feature_classes_gdb2_set):
        print(f"\nComparing feature count for: {feature_class}")
        compare_feature_counts(gdb1, gdb2, feature_class)
    
    # Step 3: If no missing feature classes, print that they are identical
    if not missing_in_gdb2 and not missing_in_gdb1:
        print("Feature classes in GDB1 and GDB2 are identical.")

def compare_feature_counts(gdb1, gdb2, feature_class):
    """
    Compare the record count of a feature class between two geodatabases.
    
    Parameters:
    - gdb1: Path to the first geodatabase
    - gdb2: Path to the second geodatabase
    - feature_class: Name of the feature class
    """
    try:
        # Get the feature count for the feature class in both geodatabases
        count_gdb1 = int(arcpy.GetCount_management(f"{gdb1}\\{feature_class}")[0])
        count_gdb2 = int(arcpy.GetCount_management(f"{gdb2}\\{feature_class}")[0])
        
        if count_gdb1 != count_gdb2:
            print(f"Record count for {feature_class} differs:")
            print(f"  GDB1 count: {count_gdb1}")
            print(f"  GDB2 count: {count_gdb2}")
        else:
            print(f"Record count matches for {feature_class}: {count_gdb1}")
    except Exception as e:
        print(f"Error comparing record count for {feature_class}: {e}")

# Usage example
gdb1 = r"C:\Users\jmcateer\Box\Fed_DOD\AFCEC\Midwest BECOS\2 - Midwest BECOS TO1and2\15.0 GIS\Grissom\DGI\Basemap-TCRA-Goby-TP\FigureGIS\GDB\GIS\GrissomARB_CTI.gdb"
gdb2 = r"C:\Users\jmcateer\Box\Fed_DOD\AFCEC\Midwest BECOS\2 - Midwest BECOS TO1and2\15.0 GIS\Grissom\DGI\Basemap-TCRA-Goby-TP\GIS\GrissomARB_CTI.gdb"


compare_feature_classes_and_counts(gdb1, gdb2)
