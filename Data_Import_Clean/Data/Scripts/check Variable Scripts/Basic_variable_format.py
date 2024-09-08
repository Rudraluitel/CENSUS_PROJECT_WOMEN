import requests

#API URL for Variable name and description. 
#base_url that contains the URL for the API endpoint you want to request.
base_url = "https://api.census.gov/data/2010/acs/acs1/subject/variables.json"

#requests.get() function fetches the data from the API and stores the response 
# in a variable named response.
response = requests.get(base_url)

#This line checks if the HTTP request was successful. response.status_code is an 
# attribute that contains the status code of the HTTP response. A status code of 200 
# means the request was successful and the server responded with the requested data.
if response.status_code == 200:
 
 #If the request was successful, this line converts the JSON data received from the
 # API into a Python dictionary. The .json() method of the response object parses 
 # the JSON response body and returns it as a Python dictionary.
 data = response.json()
 
 #This line extracts the value associated with the key 'variables' from the dictionary 
 # data and assigns it to the variable variables. This key holds the information about
 # the variables, including their IDs, names, and labels.
 variables = data['variables']
 
 #This block of code iterates over each item in the variables dictionary. The .items() 
 # method returns a view object that displays a list of a dictionary's key-value tuple 
 # pairs. variable_id represents the key of each item (i.e., the variable ID).
 """"info represents the value associated with each key (i.e., a dictionary containing 
 details about the variable....print(f"ID: {variable_id}, Name: {info['name']}, Label: 
 {info['label']}") prints the ID, name, and label of each variable.)."""
 
 for variable_id, info in variables.items():
     print(f"ID: {variable_id}, Name: {info['Name']}, Label: {info['Label']}")
     
 else: 
     print(f"Error: {response.status_code}")
 #f the request was not successful (i.e., the status code is not 200), this line prints 
 # an error message along with the status code that indicates what went wrong.    
     
 #Result:   print(f"ID: {variable_id}, Name: {info['Name']}, Label: {info['label']}")
 #since name is not present we need to fix the name function by no name function.