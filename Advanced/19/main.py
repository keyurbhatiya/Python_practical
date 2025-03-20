import csv

def process_csv(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            headers = next(reader)  # Read the header row
            data = [headers]  # Store headers
            
            for row in reader:
                processed_row = [col.upper() for col in row]  # Convert each column to uppercase
                data.append(processed_row)

        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(data)
            
        print(f"Processed CSV file saved as: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_csv = "input.csv"
output_csv = "output.csv"

# Writing sample data to input.csv
with open(input_csv, mode='w', newline='', encoding='utf-8') as infile:
    writer = csv.writer(infile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Keyur", "21", "New York"])
    writer.writerow(["Yash", "18", "Los Angeles"])
    writer.writerow(["Om", "22", "Chicago"])

process_csv(input_csv, output_csv)
