from openai import OpenAI
from reqs import open_api_key as key
from IDs.version import Version
from Training.instructionsstring_v3 import instructions_string
try:
    from IDs.OnshapeGPTID import ID
except ImportError:
    ID = None


#update Version every time model is trained
NewVersion = str(round(float(Version)+.01,2))
v = open("IDs/version.py",'w')
v.write(f"Version = \'{NewVersion}\'")
v.close()

client = OpenAI(api_key=key)
if ID is not None:
    try:
        client.beta.assistants.delete(ID)
        print('Old Assistant Deleted...')
    except:
        print('No Old Assistant Found.')
        pass
f = open('IDs/OnshapeGPTID.py','w')

file = client.files.create(file=open("Training/APIdocs.pdf", "rb"), purpose="assistants") #Need to change this so it doesn't upload a file every time

assistant = client.beta.assistants.create(
    name = "OnshapeGPT",
    description = 'Text-to-CAD solution created by Chris Tilton',
    instructions=instructions_string,
    tools=[{'type':'retrieval'}],
    file_ids=[file.id],
    model = 'gpt-4-0125-preview'
)

print(f'New Assistant Created. Updated to Version {NewVersion}.')
f.write(f'ID = \'{assistant.id}\'')