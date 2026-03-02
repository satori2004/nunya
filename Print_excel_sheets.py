""" This script reads an Excel file and prints the names of all sheets in it. """




import openpyxl

# Function to print sheet names from an Excel file
def print_sheet_names(file_path):
    try:
        # Load the Excel file
        workbook = openpyxl.load_workbook(file_path)
        
        # Get all sheet names
        sheet_names = workbook.sheetnames
        
        # Print each sheet name
        print("Sheets in the Excel file:")
        for sheet_name in sheet_names:
            print(sheet_name)
    except Exception as e:
        print(f"Error: {e}")

# Example usage
file_path = r"C:\Shared\Box\Commercial\Johnson Controls\JCI Saline, Monroe St\900-CAD-GIS\920-GIS or Graphics\Monroe_GIS\Figure_Callouts\Q4 25_DSR_SV Figure Boxes.xlsx"
print_sheet_names(file_path) 

