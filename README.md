
# OnshapeGPT
<img width="383" alt="OnshapeGPT" src="https://github.com/christilton/OnshapeGPT/assets/84406266/b19d2bbd-7e5a-446f-83fd-44199dd4e5f9">
 
OnshapeGPT is a chatbot powered by OpenAI assistants that is trained to create code that will create geometry inside a specified Onshape document. This chatbot was created and trained by Chris Tilton as a part of a Mechanical Engineering Research project under professor Chris Rogers at Tufts University in Spring 2024.

## Requirements

OnshapeGPT requires an OpenAI API Key, an Onshape API key and secret key, and an Onshape document URL stored in a file called reqs.py. The template for this can be found in reqstemplate.py.
Packages required include requests and openai.

## Current Capabilities
OnshapeGPT can create the primitive geometries (Ellipsoids, Cuboids, Cones, and Cylinders) in Onshape and combine any number of them into CAD representations of nearly anything you can think of! Will they be good representations? Who knows! OnshapeGPT has minimal fine-tuning, so it is prone to mistakes. 

## Future Additions
The next things to be added to OnshapeGPT will include analyzing the current geometry inside the Onshape document, modifying and deleting this geometry, and creating sketches and features based on these sketches.

## 
