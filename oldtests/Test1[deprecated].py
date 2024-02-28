from openai import OpenAI
client = OpenAI(api_key='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'
)


stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "You are an Onshape Expert, please generate python code to add a sketch for and extrude a 1in x 1in cube in an onshape document"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
