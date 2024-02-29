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
else:
    # Define the header for the request
    headers = {
        'Accept': 'application/vnd.onshape.v1+json',
        'Content-Type': 'application/json',
    }

    # Construct the payload to create a sphere
    create_sphere = {
        "feature": {
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
                            "expression": "3*in",
                            "parameterId": "radius"
                        }
                    }
                ]
            }
        }
    }

    # Create the sphere in Onshape
    response = requests.post(api_url, headers=headers, auth=os_api_keys, json=create_sphere)

    # Construct the payload to create a cube
    create_cube = {
        "feature": {
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
                            "expression": "5*mm",
                            "parameterId": "sideLength"
                        }
                    }
                ]
            }
        }
    }

    # Create the cube in Onshape
    response = requests.post(api_url, headers=headers, auth=os_api_keys, json=create_cube)

    # Print the result
    if response.ok:
        print("Geometries created successfully.")
    else:
        print(f"Failed to create geometries. Status code: {response.status_code}")
        print(response.text)  # Print the response content for further inspection