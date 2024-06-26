import requests
import json
from keys import os_api_keys

# Assemble the URL for the API call
url = 'https://cad.onshape.com/documents/72c8d4311f41141439a879fe/w/74a76610221425436c20fb5e/e/0d00b0248470fb8faf78f967' #Paste URL for Onshape Document Here

def convert_link(old_link):
    # Check if the old link matches the expected format
    if "cad.onshape.com/documents/" in old_link:
        # Remove 'https://' if it exists in the link
        old_link = old_link.replace("https://", "")
        
        # Split the link to extract document id, workspace id, and element id
        parts = old_link.split("/")
        doc_id = parts[2]
        workspace_id = parts[4]
        element_id = parts[6]
        
        # Construct the new link format
        new_link = f"https://cad.onshape.com/api/partstudios/d/{doc_id}/w/{workspace_id}/e/{element_id}/features"
        
        return new_link
    else:
        return "Invalid link format"
    

api_url = convert_link(url)
if api_url == "Invalid Link Format":
  print(api_url)

# Define the header for the request
headers = {
    'Accept': 'application/vnd.onshape.v1+json',
    'Content-Type': 'application/json',
}

# Construct the payload to update the Sphere's dimensions
create_sphere = {
  "feature" : {
    "type": 134,
    "typeName": "BTMFeature",
      "message": {
        "featureType": "sphere",
        "name": "Sphere1",
        "parameters": [
          {
             "type": 147,
             "typeName": "BTMParameterQuantity",
             "message": {
               "expression": "1*in",
               "parameterId": "radius"}
           }
        ]
      }
    }
}

# Create Sphere in Onshape
if api_url == "Invalid Link Format":
  print(api_url)
else:
  response = requests.post(api_url, headers=headers, auth=os_api_keys, json=create_sphere)
  print(response)

  # Check if the request was successful
  if response.ok:
      print("Geometry created successfully")
  else:
      print(f"Failed to create geometry. Status code: {response.status_code}")
      print(response.text)  # Print the response content for further inspection