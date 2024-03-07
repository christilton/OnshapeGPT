#This code was generated by OnshapeGPT V2, a chatbot trained by Chris Tilton in Spring 2023 as part of a research project under Professor Chris Rogers at Tufts University
import requests
from reqs import os_api_keys, url

def convert_link(old_link):
    if "cad.onshape.com/documents/" in old_link:
        old_link = old_link.replace("https://", "")
        parts = old_link.split("/")
        doc_id = parts[2]
        workspace_id = parts[4]
        element_id = parts[6]
        new_link = f"https://cad.onshape.com/api/partstudios/d/{doc_id}/w/{workspace_id}/e/{element_id}/"
        did_link = f"https://cad.onshape.com/api/documents/d/{doc_id}/"
        return new_link, did_link
    else:
        return "Invalid link format"

api_urls = convert_link(url)
api_url = api_urls[0]
did_link = api_urls[1]

if api_url == "Invalid link format":
  print(api_url)
else:
  headers = {
      'Accept': 'application/vnd.onshape.v1+json',
      'Content-Type': 'application/json',
  }

  # Create the first cube
  create_first_cube = {
    "feature" : {
      "type": 134,
      "typeName": "BTMFeature",
      "message": {
          "featureType": "fCuboid",
          "name": "First Cube",
          "namespace":"d2af92bf969176a0558f5f9c7::vfa91e58a301e3c528465aa9e::ef139159bebea87592e54aa0b::m6564dbd037df9a05421d9a73",
          "parameters": [
            {
               "type": 147,
               "typeName": "BTMParameterQuantity",
               "message": {
                 "expression": "vector(0,0,0)*in",
                 "parameterId": "corner1"
              }
            },
            {
               "type": 147,
               "typeName": "BTMParameterQuantity",
               "message": {
                 "expression": "vector(1,1,1)*in",
                 "parameterId": "corner2"
              }
            }
          ]
        }
      }
  }

  # Create the second cube stacked on top of the first
  create_second_cube = {
    "feature" : {
      "type": 134,
      "typeName": "BTMFeature",
      "message": {
          "featureType": "fCuboid",
          "name": "Second Cube",
          "namespace":"d2af92bf969176a0558f5f9c7::vfa91e58a301e3c528465aa9e::ef139159bebea87592e54aa0b::m6564dbd037df9a05421d9a73",
          "parameters": [
            {
               "type": 147,
               "typeName": "BTMParameterQuantity",
               "message": {
                 "expression": "vector(0,0,1)*in", # Adjusted to stack on top
                 "parameterId": "corner1"
              }
            },
            {
               "type": 147,
               "typeName": "BTMParameterQuantity",
               "message": {
                 "expression": "vector(1,1,2)*in", # Adjusted to stack on top
                 "parameterId": "corner2"
              }
            }
          ]
        }
      }
  }

  # Post the first cube
  response = requests.post(api_url+'features', headers=headers, auth=os_api_keys, json=create_first_cube)
  if response.ok:
      print("First cube created successfully.")
  else:
      print(f"Failed to create first cube. Status code: {response.status_code}")
      print(response.text)

  # Post the second cube
  response = requests.post(api_url+'features', headers=headers, auth=os_api_keys, json=create_second_cube)
  if response.ok:
      print("Second cube created successfully.")
  else:
      print(f"Failed to create second cube. Status code: {response.status_code}")
      print(response.text)

#This is the end of the Generated Code