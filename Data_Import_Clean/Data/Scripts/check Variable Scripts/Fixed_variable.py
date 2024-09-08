import requests

# API URL for variable names and descriptions
base_url = "https://api.census.gov/data/2010/acs/acs1/subject/variables.json"

response = requests.get(base_url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    variables = data.get('variables', {})
 #This line retrieves the value associated with the 'variables' key from the data 
 # dictionary. If the 'variables' key is not present, it defaults to an empty 
 # dictionary {}. This prevents errors if the key is missing.   
 # Print out the variables and their descriptions
    for variable_id, info in variables.items():
        name = info.get('name', 'No Name')
        label = info.get('label', 'No Label')
        print(f"ID: {variable_id}, Name: {name}, Label: {label}")
else:
    print(f"Error: {response.status_code}")
#we fixed the issue as name and label but we oculd not saved the data 
""""This line begins a for loop that iterates over each item in the variables dictionary.
variable_id represents the key (variable ID), and info represents the value (a dictionary 
with details about the variable

These lines use the .get() method to retrieve the values for the 'name' and 'label' keys
from the info dictionary. If either key is not present, it defaults to 'No Name' or 'No 
Label', respectively. This ensures that the code does not fail if these keys are missing.)


"""