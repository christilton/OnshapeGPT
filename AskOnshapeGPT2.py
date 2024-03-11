from openai import OpenAI
import time,sys,subprocess
from reqs import open_api_key as key
from IDs.OnshapeGPTID import ID
from IDs.version import Version

# Reference for training and calling the assistant https://towardsdatascience.com/how-to-build-an-ai-assistant-with-openai-python-8b3b5a636f69
def wait_for_assistant(thread, run):
    """
        Function to periodically check run status of AI assistant and print run time
    """
    dots = 0
    t0 = time.time()
    sys.stdout.write("\n")
    while run.status != 'completed':
        sys.stdout.write(f"\rOnshapeGPT is Thinking{'.' * dots}     ")
        sys.stdout.flush()
        dots = (dots + 1) % 6

        # retrieve status of run (this might take a few seconds or more)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        # wait 0.1 seconds
        time.sleep(0.1)
    dt = time.time() - t0
    runtime = str(round(dt,2))+" Seconds"
    sys.stdout.write('\r\033[K')
    sys.stdout.flush()
    return run, runtime

client = OpenAI(api_key=key)

thread = client.beta.threads.create()
inputstring = f"\nWelcome to OnshapeGPT Version {Version}! What would you like to create today?\n\nUser: "

#Create and add to logs
responses = open("ResponseLogs.txt",'a')
responses.write("________________________________________________________________________________________________________________________________________________________\n") 
responses.write(f"Conversation Started: {str(time.asctime(time.localtime()))}\n")
responses.write(f"Version Number:"+Version+"\n")
responses.write(f"Thread ID:{thread.id}\n")
responses.write(f"OnshapeGPT: Welcome to OnshapeGPT Version{Version}! What would you like to create today?")

try:
    while True:
        user_input = input(inputstring)
        responses.write("\nUser: "+user_input+"\n")
        message = client.beta.threads.messages.create(thread_id=thread.id, role='user', content=user_input)
        run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ID)
        run = wait_for_assistant(thread, run)
        runtime = run[1]
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        generatedresponse = messages.data[0].content[0].text.value
        responses.write(f"({runtime}) OnshapeGPT: "+generatedresponse+"\n")
        #v = open('SampleResponse.txt','w')
        #v.write(generatedresponse)
        #v.close()
        # Extract the generated response between the comments
        start_comment = f"#This code was generated by OnshapeGPT, a chatbot trained by Chris Tilton in Spring 2023 as part of a research project under Professor Chris Rogers at Tufts University"
        end_comment = "#This is the end of the Generated Code"
        if start_comment in generatedresponse:
            start_index = generatedresponse.find(start_comment)
            end_index = generatedresponse.find(end_comment) + len(end_comment)

            # Extract generated text
            generated_code = generatedresponse[start_index:end_index]

            # Extract the generated response before and after the comments
            before_comment = generatedresponse[:start_index]
            after_comment = generatedresponse[end_index:]

            # Write the extracted text to the file
            if before_comment != '':
                print("OnshapeGPT:",before_comment[:-11].strip(), flush = True,end = '\n\n')
            f = open('TextToCAD.py', 'w')
            f.write(generated_code)
            f.close()
            time.sleep(1)
            print("======================= OUTPUT FROM TEXTTOCAD.PY =======================")
            subprocess.run(['python', 'TextToCAD.py'])
            print("========================================================================")
            if after_comment != '':
                print("\nOnshapeGPT:",after_comment[5:].strip(), end = '\n')
        else:
            print('OnshapeGPT:',generatedresponse)
        inputstring = "\nUser: "
finally:
    if f is not None:
     f.close()
    responses.write("\nUser Grade (0-10):")
    responses.write("\nUser Comments:")
    responses.close()