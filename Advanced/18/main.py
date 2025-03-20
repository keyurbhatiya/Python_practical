import pandas as pd

def csv_to_html_table_pandas(csv_filename, output_filename="output.html"):
    try:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(csv_filename)
        
        # Convert DataFrame to HTML with styling
        html_content = df.to_html(classes='table', index=False)
        
        # Wrap with basic HTML structure and styling
        full_html = f"""<!DOCTYPE html>
                            <html>
                            <head>
                                <style>
                                    .table {{
                                        border-collapse: collapse;
                                        width: 100%;
                                        margin: 20px 0;
                                    }}
                                    .table th, .table td {{
                                        border: 1px solid #ddd;
                                        padding: 8px;
                                        text-align: left;
                                    }}
                                    .table th {{
                                        background-color: #f2f2f2;
                                    }}
                                    .table tr:nth-child(even) {{background-color: #f9f9f9;}}
                                    .table tr:hover {{background-color: #f5f5f5;}}
                                </style>
                            </head>
                            <body>
                                {html_content}
                            </body>
                            </html>"""
        
        # Write to output file
        with open(output_filename, 'w') as htmlfile:
            htmlfile.write(full_html)
            
        print(f"HTML table has been generated and saved as {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    csv_to_html_table_pandas("data.csv")