import requests
import json
from reqs import os_api_keys, url

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

# Construct the payload to create a Sphere with the radius of 4 inches
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
               "expression": "4 in",
               "parameterId": "radius"}
           }
        ]
      }
    }
}

# Construct the payload to create a Cube with the side length of 5 inches
create_cube = {
  "feature" : {
    "type": 134,
    "typeName": "BTMFeature",
      "message": {
        "featureType": "cube",
        "name": "Cube1",
        "parameters": [
          {
             "type": 147,
             "typeName": "BTMParameterQuantity",
             "message": {
               "expression": "5 in",
               "parameterId": "sideLength"}
           }
        ]
      }
    }
}

if api_url != "Invalid Link Format":
    # Create Sphere in Onshape
    response_sphere = requests.post(api_url, headers=headers, auth=os_api_keys, json=create_sphere)
    
    if response_sphere.ok:
        print("Sphere created successfully.")
    else:
        print(f"Failed to create sphere. Status code: {response_sphere.status_code}")
        print(response_sphere.text)  # Print the response content for further inspection

    # Create Cube in Onshape
    response_cube = requests.post(api_url, headers=headers, auth=os_api_keys, json=create_cube)
    
    if response_cube.ok:
        print("Cube created successfully.")
    else:
        print(f"Failed to create cube. Status code: {response_cube.status_code}")
        print(response_cube.text)  # Print the response content for further inspection