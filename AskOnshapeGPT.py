from openai import OpenAI
import time, subprocess
from reqs import open_api_key as key
from OnshapeGPTID import ID

#https://towardsdatascience.com/how-to-build-an-ai-assistant-with-openai-python-8b3b5a636f69

f = open('TextToCAD.py','w')

def wait_for_assistant(thread, run):
    """
        Function to periodically check run status of AI assistant and print run time
    """

    # wait for assistant process prompt
    t0 = time.time()
    while run.status != 'completed':

        # retreive status of run (this might take a few seconds or more)
        run = client.beta.threads.runs.retrieve(
          thread_id=thread.id,
          run_id=run.id
        )

        # wait 0.5 seconds
        time.sleep(0.25)
    dt = time.time() - t0
    print("Done! Elapsed time: " + str(dt) + " seconds")
    
    return run


client = OpenAI(api_key=key)

thread = client.beta.threads.create()

user_input = input("Ask OnshapeGPT to create something!\nPrompt:  ")
print('Running...')
message = client.beta.threads.messages.create(thread_id=thread.id,role='user',content=user_input)
run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=ID)
run = wait_for_assistant(thread, run)
messages = client.beta.threads.messages.list(thread_id=thread.id)
f.write(messages.data[0].content[0].text.value)
print(type(messages.data[0].content[0].text.value))
f.close()
time.sleep(1)
subprocess.run(['python','TextToCAD.py'])