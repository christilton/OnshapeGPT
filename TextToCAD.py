import requests
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
        new_link = f"https://cad.onshape.com/api/partstudios/d/{doc_id}/w/{workspace_id}/e/{element_id}/feature"
        
        return new_link
    else:
        return "Invalid Link Format"
    

api_url = convert_link(url)
if api_url == "Invalid Link Format":
  print(api_url)

# Define the header for the request
headers = {
    'Accept': 'application/vnd.onshape.v1+json',
    'Content-Type': 'application/json',
}

# Construct the payload to create the configured cube
create_configured_cube = {
    "feature": {
        "type": 134,
        "typeName": "BTMFeature",
        "message": {
            "featureType": "cube",
            "name": "Configured Cube",
            "parameters": [
                {
                    "type": 2222,
                    "typeName": "BTMParameterConfigured",
                    "message": {
                        "configurationParameterId": "Size",
                        "values": [
                            {
                                "type": 1923,
                                "typeName": "BTMConfiguredValueByEnum",
                                "message": {
                                    "namespace": "",
                                    "enumName": "Size_conf",
                                    "enumValue": "Small",
                                    "value": {
                                        "type": 147,
                                        "typeName": "BTMParameterQuantity",
                                        "message": {
                                            "expression": "2 mm"
                                        }
                                    }
                                }
                            },
                            {
                                "type": 1923,
                                "typeName": "BTMConfiguredValueByEnum",
                                "message": {
                                    "namespace": "",
                                    "enumName": "Size_conf",
                                    "enumValue": "Large",
                                    "value": {
                                        "type": 147,
                                        "typeName": "BTMParameterQuantity",
                                        "message": {
                                            "expression": "3 mm"
                                        }
                                    }
                                }
                            }
                        ],
                        "parameterId": "sideLength"
                    }
                }
            ]
        }
    }
}

# Create the configured cube in Onshape
if api_url == "Invalid Link Format":
  print(api_url)
else:
  response = requests.post(api_url, headers=headers, auth=os_api_keys, json=create_configured_cube)

  # Check if the request was successful
  if response.ok:
      print("Configured part created successfully.")
  else:
      print(f"Failed to create configured part. Status code: {response.status_code}")
      print(response.text)  # Print the response content for further inspection