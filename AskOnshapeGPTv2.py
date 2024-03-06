import time
import subprocess
import threading
from openai import OpenAI
from reqs import open_api_key as key
from OnshapeGPTID import ID

# Reference for training and calling the assistant: 
# https://towardsdatascience.com/how-to-build-an-ai-assistant-with-openai-python-8b3b5a636f69

def wait_for_assistant(client, thread, run):
    """
    Function to asynchronously check run status of AI assistant and print run time
    """
    t0 = time.time()
    while run.status != 'completed':
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        time.sleep(0.1)
    dt = time.time() - t0
    print("\nDone! Elapsed time: {:.2f} seconds".format(dt))

def spinning_wheel():
    """
    Function to display a spinning wheel while waiting for completion
    """
    while True:
        for char in '|/-\\':
            print('\rWaiting for completion ' + char, end='', flush=True)
            time.sleep(0.1)

client = OpenAI(api_key=key)
thread = client.beta.threads.create()

user_input = input("Ask OnshapeGPT to create something!\nPrompt: ")
print('Running...')

# Start the spinning wheel thread
spinner_thread = threading.Thread(target=spinning_wheel)
spinner_thread.start()

message = client.beta.threads.messages.create(thread_id=thread.id, role='user', content=user_input)
run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ID)

# Wait for the assistant run to complete asynchronously
wait_thread = threading.Thread(target=wait_for_assistant, args=(client, thread, run))
wait_thread.start()
wait_thread.join()  # Wait for the completion of the wait thread

# Stop the spinning wheel thread
spinner_thread.join()

messages = client.beta.threads.messages.list(thread_id=thread.id)

with open('TextToCAD.py', 'w') as f:
    f.write(messages.data[0].content[0].text.value)

subprocess.run(['python', 'TextToCAD.py'])
