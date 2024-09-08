import requests

# API URL for variable names and descriptions
base_url = "https://api.census.gov/data/2010/acs/acs1/subject/variables.json"

response = requests.get(base_url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    variables = data.get('variables', {})
    
    # Opens a file named census_variables.txt in write mode ("w"). The with statement 
    # ensures that the file is properly closed after writing. Writes a header line to the
    # file with tab-separated column names: ID, Name, and Label. )
    with open("census_variables.txt", "w") as file:
        # Write the header
        file.write("ID\tName\tLabel\n")
        
        # Write each variable's details
        for variable_id, info in variables.items():
            name = info.get('name', 'No Name')
            label = info.get('label', 'No Label')
            file.write(f"{variable_id}\t{name}\t{label}\n")
    #Iterates over each item in the variables dictionary. For each variable, it retrieves 
    # the name and label (with defaults if these keys are missing) and writes them to the 
    # file in a tab-separated format. Each line represents a variable's details.
    print("Variable details have been saved to 'census_variables.txt'.")
else:
    print(f"Error: {response.status_code}")
