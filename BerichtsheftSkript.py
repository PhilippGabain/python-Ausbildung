import shutil
from datetime import datetime, timedelta
from docx import Document


# Function to get Monday and Friday dates for a given week number and year
def get_monday_and_friday(year, week):
    jan_1 = datetime(year, 1, 1)
    first_monday = jan_1 + timedelta(days=(7 - jan_1.weekday()) % 7)
    monday = first_monday + timedelta(weeks=week - 1)
    friday = monday + timedelta(days=4)
    return monday, friday


# Function to copy and edit Word documents
def copy_and_edit_files(year, startweek, endweek):
    for i in range(startweek, endweek + 1):
        monday, friday = get_monday_and_friday(year, i)

        # Format dates as DD.MM.YYYY
        monday_str = monday.strftime("%d.%m.%Y")
        friday_str = friday.strftime("%d.%m.%Y")

        # Define the source file path
        source_file = "D:\\Ausbildung Berichtsheft\\ausbildungsnachweise-taeglich-data.docx"

        # Define the destination file path with the custom name
        destination_file = f"D:\\Ausbildung Berichtsheft\\täglich\\ausbildungsnachweise-taeglich-({monday.strftime('%y-%m-%d')})-({friday.strftime('%y-%m-%d')}).docx"

        try:
            # Copy the source file
            shutil.copy(source_file, destination_file)

            # Open the copied file and modify it
            doc = Document(destination_file)

            # Edit the table fields
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        if "{{DATE1}}" in cell.text:
                            cell.text = cell.text.replace("{{DATE1}}", monday_str)
                        if "{{DATE2}}" in cell.text:
                            cell.text = cell.text.replace("{{DATE2}}", friday_str)

            # Save the changes
            doc.save(destination_file)

            print(f"File copied, edited, and saved successfully to '{destination_file}'")

        except FileNotFoundError:
            print(f"Error: The source file '{source_file}' was not found.")
        except PermissionError:
            print(f"Error: Permission denied while accessing the files.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Call the function to process files
copy_and_edit_files(2025, 1, 52)
