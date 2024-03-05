from openai import OpenAI
from instructionsstring_v2 import instructions_string
from reqs import open_api_key as key
try:
    from OnshapeGPTID import ID
except ImportError:
    ID = None

client = OpenAI(api_key=key)
if ID is not None:
    try:
        client.beta.assistants.delete(ID)
        print('Old Assistant Deleted...')
    except:
        print('No Old Assistant Found.')
        pass
f = open('OnshapeGPTID.py','w')

file = client.files.create(file=open("APIdocs.pdf", "rb"), purpose="assistants")

assistant = client.beta.assistants.create(
    name = "OnshapeGPT",
    description = 'Text-to-CAD solution created by Chris Tilton',
    instructions=instructions_string,
    tools=[{'type':'retrieval'}],
    file_ids=[file.id],
    model = 'gpt-4-0125-preview'
)

print('New Assistant Created.')
f.write(f'ID = \'{assistant.id}\'')